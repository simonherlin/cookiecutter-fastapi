from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str

class UserRead(BaseModel):
    id: int
    email: str
    is_active: bool

    class Config:
        orm_mode = True
