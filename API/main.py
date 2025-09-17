from typing import Union
import models
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends, status
from database import get_db
from schemas import schemas
import crud

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users")
def read_root(db :Session = Depends(get_db)):
    return db.query(models.User).all()

@app.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/")
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)
    
@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    return crud.login(db, user)   