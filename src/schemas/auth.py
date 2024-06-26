from pydantic import BaseModel

class UserAuth(BaseModel):
    username: str
    tg_id: int


