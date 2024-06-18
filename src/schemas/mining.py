from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timedelta

class MiningStart(BaseModel):
    tg_id: int
    start_time: Optional[datetime]
    end_time: Optional[datetime]

class MiningStatus(BaseModel):
    tg_id: int
    start_time: datetime
    end_time: Optional[datetime]
    speed: float
    earned_chl: float
