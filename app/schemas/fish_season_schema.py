from pydantic import BaseModel


class FishSeasonBase(BaseModel):
    pass 


class FishSeasonCreate(FishSeasonBase):
    pass


class FishSeasonUpdate(FishSeasonBase):
    pass


class FishSeasonResponse(FishSeasonBase):
    pass