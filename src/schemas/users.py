from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    tg_id: int
    first_name: str
    language_code: str

class UserLogin(BaseModel):
    password: str


