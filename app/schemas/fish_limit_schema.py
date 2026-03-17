from pydantic import BaseModel
from app.enums.region_type import RegionType


class FishLimitBase(BaseModel):
    min_size_inches: float | None  
    max_size_inches: float | None  
    limit_amount: int | None 
    region: str 
    region_type: RegionType = RegionType.STATEWIDE


class FishLimitCreate(FishLimitBase):
    species_id: int


class FishLimitUpdate(BaseModel):
    min_size_inches: float | None  = None
    max_size_inches: float | None  = None
    limit_amount: int | None = None
    region: str | None = None
    region_type: RegionType | None = None


class FishLimitResponse(FishLimitBase):
    id: int 
    species_id: int

    class Config:
        from_attributes = True