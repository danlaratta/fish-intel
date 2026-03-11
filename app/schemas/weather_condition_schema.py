from pydantic import BaseModel
from datetime import datetime


class WeatherConditionBase(BaseModel):
    wind_speed: int 
    wind_direction_degrees: float
    air_temp: int 
    air_pressure: float
    weather_code: int
    


class WeatherConditionCreate(WeatherConditionBase):
    fishing_spot_id: int


class WeatherConditionResponse(WeatherConditionBase):
    id: int 
    fishing_spot_id: int
    created_at: datetime

    class Config:
        from_attributes = True