from pydantic import BaseModel


class FishingSpotBase(BaseModel):
    pass 


class FishingSpotCreate(FishingSpotBase):
    pass


class FishingSpotUpdate(FishingSpotBase):
    pass


class FishingSpotResponse(FishingSpotBase):
    id: int 

    class Config:
        from_attributes = True