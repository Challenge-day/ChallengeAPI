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
    """
    db_mining = await repository_mining.start_mining(db, mining_start.tg_id)
    return db_mining

@router.get("/get_mining_status/{tg_id}", response_model=MiningStatus)
async def update_mining_status_endpoint(tg_id: str, db: Session = Depends(get_db)):
    """
    Updates the mining status for the user with the given Telegram ID.
    
    Args:
        tg_id (str): The Telegram ID of the user.
        db (Session): The database session.
    
    Returns:
        MiningStatus: The updated mining status.
    
    Raises:
        HTTPException: If the mining session is not found.
    """
    db_mining = await repository_mining.update_mining_status(db, tg_id)
    if not db_mining:
        raise HTTPException(status_code=404, detail="Mining session not found")
    return db_mining