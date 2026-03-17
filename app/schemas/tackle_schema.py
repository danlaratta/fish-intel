from pydantic import BaseModel
from app.enums.lure_type import LureType
from app.enums.tackle_type import TackleType


class TackleBase(BaseModel):
    name: str
    tackle_type: TackleType
    lure_type: LureType | None
    color: str | None 
    lure_size: str | None 
    jig_head_size: str | None 


class TackleCreate(TackleBase):
    pass


class TackleResponse(TackleBase):
    id: int 

    class Config:
        from_attributes = True