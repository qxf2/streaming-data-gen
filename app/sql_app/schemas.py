from pydantic import BaseModel
from typing import Union

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    full_name: Union[str, None] = None

    class Config:
        orm_mode = True