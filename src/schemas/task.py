from pydantic import BaseModel

class TaskCreate(BaseModel):
    name: str
    description: str

class TaskResponse(BaseModel):
    id: int
    name: str
    description: str
    completed: bool
    user_id: int

    class Config:
        orm_mode = True