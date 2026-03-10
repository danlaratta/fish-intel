from pydantic import BaseModel


class MarineWeatherConditionBase(BaseModel):
    pass 


class MarineWeatherConditionCreate(MarineWeatherConditionBase):
    pass


class MarineWeatherConditionUpdate(MarineWeatherConditionBase):
    pass


class MarineWeatherConditionResponse(MarineWeatherConditionBase):
    id: int 

    class Config:
        from_attributes = True