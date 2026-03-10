from pydantic import BaseModel


class FishingScoreHourlyBase(BaseModel):
    pass 


class FishingScoreHourlyCreate(FishingScoreHourlyBase):
    pass


class FishingScoreHourlyUpdate(FishingScoreHourlyBase):
    pass


class FishingScoreHourlyResponse(FishingScoreHourlyBase):
    id: int 

    class Config:
        from_attributes = True