from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.schemas.auth import UserAuth
from src.db.connect import get_db

from src.models.entity import Auth

router = APIRouter()

@router.post("/auth/{tg_id}", response_model=UserAuth)
async def get_auth(tg_id: int, db: Session = Depends(get_db)):
    auth = db.query(Auth).filter(Auth.tg_id == tg_id).first()
    if not auth:
        raise HTTPException(status_code=404, detail="Auth data not found")
    return UserAuth(username=auth.username, tg_id=auth.tg_id)