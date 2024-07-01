from pydantic import BaseModel


class UserCreate(BaseModel):
    telegram_id: int
    first_name: str
    last_name: str
    username: str
    language_code: str
