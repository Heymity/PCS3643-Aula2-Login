from typing import Union
import models
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException, Depends, status
from database import get_db


app = FastAPI()

@app.get("/")
def read_root(db :Session = Depends(get_db)):
    return db.query(models.User).all()


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

