from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.schemas.mining import MiningStart, MiningStatus
from src.repositories import mining as repository_mining
from src.db.connect import get_db

router = APIRouter()

@router.post("/start_mining", response_model=MiningStart)
async def start_mining_endpoint(mining_start: MiningStart, db: Session = Depends(get_db)):
    """
    Starts a new mining session for the user with the given Telegram ID.
    
    Args:
        mining_start (MiningStart): The mining start request containing the Telegram ID.
        db (Session): The database session.
    
    Returns:
        MiningStart: The created mining session.
    
    Raises:
        HTTPException: If the Telegram ID is invalid or if there is an error creating the session.
    """
    try:
        db_mining = await repository_mining.start_mining(db, mining_start.telegram_id)
        return db_mining
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    

@router.get("/get_mining_status/{telegram_id}", response_model=MiningStatus)
async def get_mining_status_endpoint(telegram_id: int, db: Session = Depends(get_db)):
    """
    Gets the mining status for the user with the given Telegram ID.
    
    Args:
        telegram_id (int): The Telegram ID of the user.
        db (Session): The database session.
    
    Returns:
        MiningStatus: The current mining status.
    
    Raises:
        HTTPException: If the mining session is not found.
    """
    try:
        db_mining = await repository_mining.update_mining_status(db, telegram_id)
        if not db_mining:
            raise HTTPException(status_code=404, detail="Mining session not found")
        return db_mining
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="An error occurred while retrieving the mining status")