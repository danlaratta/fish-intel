from pydantic import BaseModel


class WeatherConditionBase(BaseModel):
    pass 


class WeatherConditionCreate(WeatherConditionBase):
    pass


class WeatherConditionUpdate(WeatherConditionBase):
    pass


class WeatherConditionResponse(WeatherConditionBase):
    id: int 

    class Config:
        from_attributes = True