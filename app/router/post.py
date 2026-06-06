from sqlalchemy.exc import IntegrityError
from app import oauth2
from .. import utils, schemas, models
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List


router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)



@router.get("/", response_model=List[schemas.PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: schemas.TokenData = Depends(
        oauth2.get_current_user
    )):
    posts = db.query(models.Post).all()

    return posts


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.PostResponse
)
def create_post(
    post: schemas.PostCreate,
    db: Session = Depends(get_db),
    user_id: schemas.TokenData = Depends(
        oauth2.get_current_user
    )
):
    new_post = models.Post(
        title=post.title,
        content=post.content,
        published=post.published,
        owner_id = user_id.id
        
    )

    db.add(new_post)

    db.commit()

    db.refresh(new_post)

    return new_post

@router.get(
    "/{id}",
    response_model=schemas.PostResponse
)
def get_post(
    id: int,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(
        oauth2.get_current_user)
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


@router.delete("/{id}")
def delete_post( 
    id: int,
    db: Session = Depends(get_db) ,
    current_user: schemas.TokenData = Depends(
        oauth2.get_current_user
    )
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

    if post.owner_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not authorized to perform requested action"
        )

    post_query.delete(
        synchronize_session=False
    )

    db.commit()

    return {
        "message": "Post deleted successfully"
    }

@router.put(
    "/{id}",
    response_model=schemas.PostResponse
)
def update_post(
    id: int,
    updated_post: schemas.PostCreate,
    db: Session = Depends(get_db),
    current_user: schemas.TokenData = Depends(
        oauth2.get_current_user)
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

    if post.owner_id != current_user.id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not authorized to perform requested action"
            )
    db.commit()

    return post_query.first()


















