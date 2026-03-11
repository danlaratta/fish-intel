from pydantic import BaseModel


class FishSpeciesBase(BaseModel):
    name: str  


class FishSpeciesCreate(FishSpeciesBase):
    pass


class FishSpeciesResponse(FishSpeciesBase):
    id: int 

    class Config:
        from_attributes = True