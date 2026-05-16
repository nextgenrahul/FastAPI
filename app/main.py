from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
import psycopg2.extras 



app = FastAPI()
try:
    conn = psycopg2.connect(
        host='localhost',
        database='fastapi',
        user='postgres',
        password='admind1234',
        port=5433,
        cursor_factory=psycopg2.extras.RealDictCursor
    )
    cursor = conn.cursor()
    print("Database connection successful")

except Exception as error:
    print("Database connection failed")
    print("Error:", error)
    
class Post(BaseModel):
    name : str
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
    return {"data" : my_post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
async def create_post(new_post : Post):
    post_dict = new_post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_post.append(post_dict)
    return {'data' : post_dict}

 
@app.get("/posts/latest")
def get_latest_post():
     post = my_post[len(my_post)  - 1]
     return {"data" : post} 

@app.get("/posts/{id}")
def get_post(id : int, response : Response):
     post = find_post(id) 
     if not post:
        #  response.status_code = status.HTTP_404_NOT_FOUND 
        #  return {"message" : f"Post with id : {id} was not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id : {id} was not found")
     return {"post_details": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post was not found"
        )

    my_post.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

from fastapi import HTTPException, status


@app.put("/posts/{id}")
def update_post(id: int, updated_post: Post):

    index = find_index_post(id)

    if index is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post was not found"
        )

    post_dict = updated_post.dict()
    post_dict["id"] = id

    my_post[index] = post_dict

    return {
        "message": "Post updated successfully",
        "data": my_post[index]
    }