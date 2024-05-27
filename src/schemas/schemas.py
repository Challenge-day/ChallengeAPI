from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    telegram_id: int
    first_name: str
    language_code: str

class UserLogin(BaseModel):
    email: str
    password: str

class MessageCreate(BaseModel):
    message_id: int
    user_id: int
    chat_id: int
    text: str
    command: Optional[str] = None

class MessageResponse(BaseModel):
    id: int
    message_id: int
    user_id: int
    chat_id: int
    text: str
    command: Optional[str]

    class Config:
        from_attributes = True
