from pydantic import BaseModel


class CatchLogBase(BaseModel):
    length_inches: float 
    weight_lb: float | None 
    released: bool


class CatchLogCreate(CatchLogBase):
    user_id: int
    fishing_session_id: int
    species_id: int
    tackle_id: int
    fishing_spot_id: int


class CatchLogResponse(CatchLogBase):
    id: int 
    user_id: int
    fishing_session_id: int
    species_id: int
    tackle_id: int
    fishing_spot_id: int

    class Config:
        from_attributes = True