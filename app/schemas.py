
from datetime import datetime
from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True


class PostCreate(PostBase):
    pass


class PostResponse(PostBase):
    id: int

    class Config:
        from_attributes = True


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
    id: str | None = None