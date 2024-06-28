from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.models.entity import Referral
from src.db.connect import get_db
from src.services.referral_service import generate_referral_url, handle_referral

router = APIRouter()

@router.get("/generate_referral_url/{telegram_id}")
def get_referral_url(telegram_id: int, db: Session = Depends(get_db)):
    """
    The get_referral_url function generates a referral url for the user with telegram_id.
        The function returns a JSON object containing the generated referral url.
    
    :param telegram_id: int: Tell the function that it will receive an integer as a parameter
    :param db: Session: Get the database session
    :return: A referral url for a given user
    """
    url = generate_referral_url(telegram_id, db)
    return {"referral_url": url}

@router.get("/referral/{telegram_id}")
async def referral(telegram_id: int, db: Session = Depends(get_db)):
    """
    The referral function is used to handle referrals.
    It takes a telegram id and returns a message indicating whether the referral was successful or not.
    
    :param telegram_id: int: Pass the telegram user id to the function
    :param db: Session: Pass the database connection to the function
    :return: A message, but the user function returns a user object
    """
    user = await handle_referral(telegram_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User {user.username} referred successfully"}