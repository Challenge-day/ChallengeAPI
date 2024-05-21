from pydantic import BaseModel
from typing import List
from .task import TaskResponse

class UserResponse(BaseModel):
    id: int
    tg_id: int
    username: str
    first_name: str
    last_name: str
    points: int
    tasks: List[TaskResponse]

    class Config:
        orm_mode = True