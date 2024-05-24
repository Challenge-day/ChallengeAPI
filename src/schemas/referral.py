from pydantic import BaseModel
from datetime import datetime

class Referral(BaseModel):
    referrer_id: int
    referred_id: int

class ReferralResponse(BaseModel):
    id: int
    is_active: bool
    referrer_id: int
    referred_id: int
    created_at: datetime

    class Config:
        orm_mode = True