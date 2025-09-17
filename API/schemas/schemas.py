from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
        email: EmailStr
        username: str
        nome: str
        

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
        email: str
        password: str


class UserResponse(UserBase):
        id: int

class Config:
         orm_mode = True