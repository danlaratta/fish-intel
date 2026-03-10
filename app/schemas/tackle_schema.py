from pydantic import BaseModel


class TackleBase(BaseModel):
    pass 


class TackleCreate(TackleBase):
    pass


class TackleUpdate(TackleBase):
    pass


class TackleResponse(TackleBase):
    pass