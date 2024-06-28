from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.users import UserCreate
from src.models.entity import User
from src.db.connect import get_db

router = APIRouter()


@router.get("/users/{telegram_id}")
async def get_user_by_telegram_id(telegram_id: int, db: Session = Depends(get_db)):
    
    user = User.get_user_by_telegram_id(db, telegram_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/users")
async def create_user(user_info: UserCreate, db: Session = Depends(get_db)):
    existing_user = User.get_user_by_telegram_id(db, user_info.telegram_id)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    new_user = User(
        telegram_id=user_info.telegram_id,
        first_name=user_info.first_name,
        last_name=user_info.last_name,
        username=user_info.username,
        language_code=user_info.language_code
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
