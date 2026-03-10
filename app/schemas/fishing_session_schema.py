from pydantic import BaseModel


class FishingSessionBase(BaseModel):
    pass 


class FishingSessionCreate(FishingSessionBase):
    pass


class FishingSessionUpdate(FishingSessionBase):
    pass


class FishingSessionResponse(FishingSessionBase):
    pass