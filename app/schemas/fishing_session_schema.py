from pydantic import BaseModel
from datetime import datetime
from app.enums.fishing_method import FishingMethod


class FishingSessionBase(BaseModel):
    session_start: datetime  
    session_end: datetime  
    fishing_method: FishingMethod
    updated_at: datetime | None 


class FishingSessionCreate(FishingSessionBase):
    fishing_spot_id: int 


class FishingSessionUpdate(FishingSessionBase):
    updated_at: datetime | None


class FishingSessionResponse(FishingSessionBase):
    id: int 
    user_id: int 
    fishing_spot_id: int 

    class Config:
        from_attributes = True