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


class FishSeasonUpdate(BaseModel):
    season_start: date | None = None
    season_end: date | None = None
    region: str | None = None 
    region_type: RegionType | None = None 


class FishSeasonResponse(FishSeasonBase):
    id: int 
    species_id: int

    class Config:
        from_attributes = True