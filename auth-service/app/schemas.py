from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    full_name: str

class UserOut(BaseModel):
    id: str
    email: EmailStr
    full_name: str

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
