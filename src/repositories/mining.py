from sqlalchemy.orm import Session
from src.models.entity import MiningSession
from datetime import datetime, timedelta
from src.services.mining_service import calculate_earned_chl_since_last_check

async def start_mining(db: Session, telegram_id: int):
    """
    Starts a new mining session for the user with the given Telegram ID (telegram_id).
    
    The mining session is set to last for 4 hours, with an initial mining speed of 2.5. The session is persisted to the database using the provided SQLAlchemy session (db).
    
    Args:
        db (Session): The SQLAlchemy session to use for database operations.
        telegram_id (int): The Telegram ID of the user for whom to start the mining session.
    
    Returns:
        MiningSession: The newly created mining session object.
    """
    end_time = datetime.now() + timedelta(hours=4)
    speed = 2.5
    db_mining = MiningSession(
        telegram_id=telegram_id, start_time=datetime.now(), 
        end_time=end_time, 
        speed=speed
        )
    db.add(db_mining)
    db.commit()
    db.refresh(db_mining)
    return db_mining

async def get_mining_session(db: Session, telegram_id: int):
    """
    Retrieves the most recent mining session for the user with the given Telegram ID (telegram_id).
    
    Args:
        db (Session): The SQLAlchemy session to use for database operations.
        telegram_id (int): The Telegram ID of the user for whom to retrieve the mining session.
    
    Returns:
        MiningSession: The most recent mining session for the given user, or None if no session exists.
    """
    return db.query(MiningSession).filter(MiningSession.telegram_id == telegram_id).order_by(MiningSession.start_time.desc()).first()

async def update_mining_status(db: Session, telegram_id: int):
    """
    Updates the mining status for the user with the given Telegram ID (telegram_id).
    
    This function retrieves the most recent mining session for the user, calculates the amount of CHL earned since the last check, updates the earned CHL and last checked time in the mining session, and adjusts the mining speed based on the elapsed time. The updated mining session is then committed to the database.
    
    Args:
        db (Session): The SQLAlchemy session to use for database operations.
        telegram_id (int): The Telegram ID of the user for whom to update the mining status.
    
    Returns:
        MiningSession: The updated mining session object.
    """
    mining_session = get_mining_session(db, telegram_id)
    if not mining_session:
        return None
    current_time = datetime.now()
    earned_chl = calculate_earned_chl_since_last_check(mining_session.start_time, current_time, mining_session.last_checked)
    mining_session.earned_chl += earned_chl
    mining_session.last_checked = current_time

    # Update cuurent time in depending on the mining speed
    elpased_time = (current_time - mining_session.start_time).total_seconds() / 3600.0
    if elpased_time > 12:
        mining_session.speed = 1.0
    elif elpased_time > 8:
        mining_session.speed = 3.90625
    elif elpased_time > 4:
        mining_session.speed = 3.125
    else:
        mining_session.speed = 2.5
    db.commit()
    db.refresh(mining_session)
    return mining_session



