from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.entity import User
from src.repositories.users import start
from src.db.connect import get_db
from src.schemas.users import UserCreate

router = APIRouter()

# @router.post("/users/", response_model=UserCreate)
# def create_user(user: UserCreate, db: Session = Depends(get_db)):
#     """
#     Create a new user in the system.

#     - **name**: The user's username
#     - **chat_id**: The user's Telegram chat ID
#     - **first_name**: The user's first name
#     - **language_code**: The user's language code
#     """
#     user_repo = start(db)
#     db_user = user_repo.get_by_tg_id(user.chat_id)
#     if db_user:
#         raise HTTPException(status_code=400, detail="User already registered")
    
#     new_user = User(
#         username=user.username,
#         chat_id=user.chat_id,
#         first_name=user.first_name,
#         language_code=user.language_code
#     )

#     user_repo.add(new_user)
#     return new_user


@router.post("/users/{chat_id}")
async def get_user_by_chat_id(chat_id: int, db: Session = Depends(get_db)):
    user = User.get_user_by_chat_id(db, chat_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
