from pydantic import BaseModel
from datetime import date
from app.enums.region_type import RegionType


class FishSeasonBase(BaseModel):
    season_start: date | None 
    season_end: date | None 
    region: str 
    region_type: RegionType = RegionType.STATEWIDE 


class FishSeasonCreate(FishSeasonBase):
    species_id: int


class FishSeasonUpdate(FishSeasonBase):
    season_start: date | None 
    season_end: date | None 


class FishSeasonResponse(FishSeasonBase):
    id: int 
    species_id: int

    class Config:
        from_attributes = True