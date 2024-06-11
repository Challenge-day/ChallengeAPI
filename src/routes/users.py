from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.entity import User
from src.repositories.users import UserRepository
from src.db.connect import get_db
from src.schemas.users import UserCreate, UserLogin

router = APIRouter()

@router.post("/users/", response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user in the system.

    - **username**: The user's username
    - **password**: The user's password
    - **telegram_id**: The user's Telegram ID
    - **first_name**: The user's first name
    - **language_code**: The user's language code
    """
    user_repo = UserRepository(db)
    db_user = user_repo.get_by_tg_id(user.tg_id)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    
    new_user = User(
        username=user.username,
        password=user.password,
        tg_id=user.tg_id,
        first_name=user.first_name,
        language_code=user.language_code
    )

    user_repo.add(new_user)
    return new_user

@router.post("/login/")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate a user and provide access to the application.

    - **email**: The user's email address
    - **password**: The user's password
    """
    user_repo = UserRepository(db)
    if user_repo.validate_user(user.password):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=400, detail="Invalid credentials")