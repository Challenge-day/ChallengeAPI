from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.auth import UserAuth
from src.db.connect import get_db

from src.models.entity import Auth

router = APIRouter()

@router.get("/auth/{telegram_id}", response_model=UserAuth)
async def get_auth(telegram_id: int, db: Session = Depends(get_db)):
    auth = db.query(Auth).filter(Auth.telegram_id == telegram_id).first()
    if not auth:
        raise HTTPException(status_code=404, detail="Auth data not found")
    return UserAuth(username=auth.username, telegram_id=auth.telegram_id)


@router.post("/auth", response_model=UserAuth)
async def create_auth(auth_data: UserAuth, db: Session = Depends(get_db)):
    auth = Auth(username=auth_data.username, telegram_id=auth_data.telegram_id)
    db.add(auth)
    db.commit()
    db.refresh(auth)
    return UserAuth(username=auth.username, telegram_id=auth.telegram_id)