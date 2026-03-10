from pydantic import BaseModel


class TideBase(BaseModel):
    pass 


class TideCreate(TideBase):
    pass


class TideUpdate(TideBase):
    pass


class TideResponse(TideBase):
    id: int 

    class Config:
        from_attributes = True