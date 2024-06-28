from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    tg_id: int
    first_name: str
    language_code: str


