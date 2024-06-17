from pydantic import BaseModel

class UserAuth(BaseModel):
    username: str
    chat_id: int


