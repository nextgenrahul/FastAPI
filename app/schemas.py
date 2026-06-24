from typing import Annotated

from pydantic import BaseModel, ConfigDict, Field, conint

from datetime import datetime
from pydantic import BaseModel, EmailStr, conint


    
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime
    is_active: bool

    class Config:
        from_attributes = True
        

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token : str
    token_type : str
    
class TokenData(BaseModel):
    id: int | None = None
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserResponse
    
    class Config:
        from_attributes = True


class PostOut(BaseModel):
    Post: PostResponse
    votes: int

    model_config = ConfigDict(
        from_attributes=True
    )

class Vote(BaseModel):
    post_id: int
    dir: Annotated[int, Field(ge=0, le=1)]