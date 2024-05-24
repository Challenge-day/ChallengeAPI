from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    telegram_id: int
    first_name: str
    language_code: str

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
        orm_mode = True
