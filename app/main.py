from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models
from app import schemas


from app.database import engine, get_db

from app.utils import hash_password

from sqlalchemy.exc import IntegrityError



app = FastAPI()

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    
    return {"message": "FastAPI + PostgreSQL + SQLAlchemy"}
