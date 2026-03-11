from pydantic import BaseModel
from datetime import datetime


class FishingScoreHourlyBase(BaseModel):
    hour: datetime 
    score: int  


class FishingScoreHourlyCreate(FishingScoreHourlyBase):
    fishing_spot_id: int 


class FishingScoreHourlyResponse(FishingScoreHourlyBase):
    id: int 
    fishing_spot_id: int 

    class Config:
        from_attributes = True