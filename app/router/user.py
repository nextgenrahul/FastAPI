
from psycopg2 import IntegrityError
from .. import utils, schemas, models
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate, db: Session = Depends(get_db)):
    password = utils.hash_password(user.password)
    new_user = models.User(
        email=user.email, 
        password=password
    )
    try:
        db.add(new_user)
        db.commit() 
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already exists"
        )
        

@router.get('/users/{id}', response_model=schemas.UserResponse)
def get_user(id: int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details=f"User with id : {id} does not exist")
    return user


