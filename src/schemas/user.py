from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class UserLoginModel(BaseModel):
    email: EmailStr = 'user@gmail.com'
    password: str = 'qwerty'