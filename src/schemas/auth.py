from pydantic import BaseModel


class UserAuth(BaseModel):
    username: str
    telegram_id: int
