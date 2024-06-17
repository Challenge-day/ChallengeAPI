from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    chat_id: int
    first_name: str
    language_code: str


