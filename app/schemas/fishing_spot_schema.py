from pydantic import BaseModel


class FishingSpotBase(BaseModel):
    name: str 
    longitude: float 
    latitude: float 
    description: str | None = None 


class FishingSpotCreate(FishingSpotBase):
    pass


class FishingSpotResponse(FishingSpotBase):
    id: int 
    user_id: int 

    class Config:
        from_attributes = True