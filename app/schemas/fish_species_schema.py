from pydantic import BaseModel


class FishSpeciesBase(BaseModel):
    pass 


class FishSpeciesCreate(FishSpeciesBase):
    pass


class FishSpeciesUpdate(FishSpeciesBase):
    pass


class FishSpeciesResponse(FishSpeciesBase):
    id: int 

    class Config:
        from_attributes = True