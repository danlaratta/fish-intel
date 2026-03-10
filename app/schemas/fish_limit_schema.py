from pydantic import BaseModel


class FishLimitBase(BaseModel):
    pass 


class FishLimitCreate(FishLimitBase):
    pass


class FishLimitUpdate(FishLimitBase):
    pass


class FishLimitResponse(FishLimitBase):
    pass