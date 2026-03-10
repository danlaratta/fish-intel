from pydantic import BaseModel


class CatchLogBase(BaseModel):
    length_inches: float 
    weight_lb: float | None 
    released: bool


class CatchLogCreate(CatchLogBase):
    pass


class CatchLogResponse(CatchLogBase):
    id: int 

    class Config:
        from_attributes = True