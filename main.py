from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()
class Post(BaseModel):
    name : str
    company : str
    rating : Optional[int] = None
    

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/createposts")
async def create_post(new_post : Post):
    print(new_post.name)
    # return {'message' : f"Name : {new_post.name},  Company : {new_post.company}"}
    return new_post