from ast import While
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
import psycopg2.extras
import time

app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(
            host='localhost',
            database='fastapi',
            user='postgres',
            password='admin1234',
            port=5433,
            cursor_factory=psycopg2.extras.RealDictCursor
        )

        cursor = conn.cursor()

        print("Database connection successful")
        break

    except Exception as error:
        print("Database connection failed")
        print("Error:", error)

        time.sleep(2)
        
class Post(BaseModel):
    title : str
    content : str
    published: bool = True
    rating : int | None = None
        
my_post = [
    {
        "title": "title of post1",
        "content": "post 1 content",
        "id": 1
    },
    {
        "title": "title of post2",
        "content": "post 2 content",
        "id": 2
    },
    {
        "title": "title of post3",
        "content": "post 3 content",
        "id": 3
    }
]

def find_post(id):
    for p in my_post:
        if p["id"] == id:
            return p

def find_index_post(id):
    for i, p in enumerate(my_post):
        if p["id"] == id:
            return i



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/posts")
def read_root():
    cursor.execute("""SELECT * FROM posts""")
    posts = cursor.fetchall()
    print(posts)
    return {"Data": posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(posts: Post):
    cursor.execute(
        """INSERT INTO posts (title, content, published)
        VALUES (%s, %s, %s)
        RETURNING *""",
        (posts.title, posts.content, posts.published)
    )
    new_post = cursor.fetchone()

    conn.commit()

    return {'data': new_post}

 
@app.get("/posts/latest")
def get_latest_post():
     post = my_post[len(my_post)  - 1]
     return {"data" : post} 

@app.get("/posts/{id}")
def get_post(id : int, response : Response):
    cursor.execute(
    """SELECT * FROM posts WHERE id = %s """, (id,)
    )
    post = cursor.fetchone()

    conn.commit()
    
    
    
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id : {id} was not found")
    return {"post_details": post}


@app.delete("/posts/{id}")
def delete_post(id: int):

    cursor.execute(
        """DELETE FROM posts WHERE id = %s RETURNING *""",
        (id,)
    )

    deleted_post = cursor.fetchone()

    conn.commit()

    if deleted_post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found"
        )

    return {
        "message": "Post deleted successfully",
        "deleted_post": deleted_post
    }

@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post):

    cursor.execute(
        """
        UPDATE posts
        SET title = %s,
            content = %s,
            published = %s
        WHERE id = %s
        RETURNING *
        """,
        (
            updated_post.title,
            updated_post.content,
            updated_post.published,
            id
        )
    )

    post = cursor.fetchone()

    conn.commit()

    if post is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {id} was not found"
        )

    return {
        "message": "Post updated successfully",
        "data": post
    }