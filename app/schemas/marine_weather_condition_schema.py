from pydantic import BaseModel
from datetime import datetime


class MarineWeatherConditionBase(BaseModel):
    water_temp: float 
    wave_height: float 


class MarineWeatherConditionCreate(MarineWeatherConditionBase):
    pass


class MarineWeatherConditionResponse(MarineWeatherConditionBase):
    id: int 
    fishing_spot_id: int
    created_at: datetime

    class Config:
        from_attributes = True