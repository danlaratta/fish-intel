from pydantic import BaseModel
from datetime import datetime
from app.enums.tide import Tide


class TideBase(BaseModel):
    tide: Tide 
    tide_time: datetime 


class TideCreate(TideBase):
    pass


class TideResponse(TideBase):
    id: int 
    fishing_spot_id: int 

    class Config:
        from_attributes = True