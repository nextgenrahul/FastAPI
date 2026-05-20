from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models
from app import schemas

from app.database import engine, get_db

app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    
    return {"message": "FastAPI + PostgreSQL + SQLAlchemy"}


@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):

    posts = db.query(models.Post).all()

    return {"data": posts}


@app.post(
    "/posts",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PostResponse
)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db)
):

    new_post = models.Post(
        title=post.title,
        content=post.content,
        published=post.published
    )

    db.add(new_post)

    db.commit()

    db.refresh(new_post)

    return new_post


@app.get(
    "/posts/{id}",
    response_model=schemas.PostResponse
)
def get_post(
    id: int,
    db: Session = Depends(get_db)
):

    post = db.query(models.Post).filter(
        models.Post.id == id
    ).first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    return post


@app.delete("/posts/{id}")
def delete_post(
    id: int,
    db: Session = Depends(get_db)
):

    post_query = db.query(models.Post).filter(
        models.Post.id == id
    )

    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    post_query.delete(
        synchronize_session=False
    )

    db.commit()

    return {
        "message": "Post deleted successfully"
    }


@app.put(
    "/posts/{id}",
    response_model=schemas.PostResponse
)
def update_post(
    id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db)
): 

    post_query = db.query(models.Post).filter(
        models.Post.id == id
    )

    post = post_query.first()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} not found"
        )

    post_query.update(
        updated_post.dict(),
        synchronize_session=False
    )

    db.commit()

    return post_query.first()