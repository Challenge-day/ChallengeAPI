from sqlalchemy.orm import Session
from src.models.entity import User, Referral

def generate_referral_url(tg_id: int) -> str:
    """
    The generate_referral_url function takes a Telegram user ID and returns a referral URL.
    The referral URL is used to invite new users to the bot.
    
    
    :param tg_id: int: Specify the type of parameter that is expected to be passed into the function
    :return: A referral link
    """
    return f"https://t.me/challenge-day?start={tg_id}"

async def handle_referral(tg_id: int, db: Session) -> User:
    """
    The handle_referral function is used to handle a referral.
    It takes in the tg_id of the user who was referred and a database session object.
    If there is no referrer, it returns None. Otherwise, it creates a new User object for the referred user and adds them to 
    the database session before committing their addition to the database. It then refreshes that User object from 
    the database so that we can get its id attribute (which will be auto-generated by SQLAlchemy). Finally, it creates 
    a Referral object with both users' IDs and commits this addition as well.
    
    :param tg_id: int: Identify the user that referred the new user
    :param db: Session: Pass the database session to the function
    :return: A user object
    """
    referrer = db.query(User).filter(User.tg_id == tg_id).first()
    if not referrer:
        return None
    referred_user = User(tg_id=tg_id, username=f"user_{tg_id}")
    db.add(referred_user)
    db.commit()
    db.refresh(referred_user)

    referral = Referral(referrer_id=referrer.id, referred_id=referred_user.id)
    db.add(referral)
    db.commit()
    return referred_user