from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from sqlalchemy import select
from schemas import schemas
import models 

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        nome=user.nome,
        email=user.email,
        password=user.password 
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def login(db: Session, user: schemas.UserCreate):
    try:
        s = select(models.User).where(models.User.email == user.email)
        return db.scalars(s).one().password == user.password
    except (NoResultFound):
        return False
   

  
def get_users(db: Session):
    return db.query(models.User).all()
