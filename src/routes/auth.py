from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.auth import UserAuth
from src.db.connect import get_db

from src.models.entity import Auth, User

router = APIRouter()

    
@router.post("/auth/", response_model=UserAuth)
async def create_auth(user_auth: UserAuth, db: Session = Depends(get_db)):
    """
    Authorization a new user in the system.

    - **name**: The user's username
    - **chat_id**: The user's Telegram chat ID
    """
    try:
        # проверяем, существует ли пользователь с таким chat_id в базе данных
        user = db.query(User).filter(User.chat_id == user_auth.chat_id).first()
        if user is None:
            raise HTTPException(status_code=404, detail="User not found")
        
        new_auth = Auth(name=user_auth.name, chat_id=user_auth.chat_id)
        db.add(new_auth)
        db.commit()
        return {f"message": "Authentication {user_auth} successful"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))