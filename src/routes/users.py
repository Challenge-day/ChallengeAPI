from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session

from src.models.entity import User
from src.db.connect import get_db

router = APIRouter()

@router.post("/users/{chat_id}")
async def get_user_by_chat_id(chat_id: int, db: Session = Depends(get_db)):
    user = User.get_user_by_chat_id(db, chat_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
