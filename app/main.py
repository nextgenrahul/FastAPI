from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas

from app.database import engine, get_db

from app.utils import hash_password

from sqlalchemy.exc import IntegrityError

from .router import post, user, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()
 
app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL + SQLAlchemy"}
  