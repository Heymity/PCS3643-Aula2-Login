from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "usuarios"
    __table_args__ = {'schema': 'api'}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String, index=True)
    username = Column(String, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)