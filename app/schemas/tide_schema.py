from pydantic import BaseModel


class TideBase(BaseModel):
    pass 


class TideCreate(TideBase):
    pass


class TideUpdate(TideBase):
    pass


class TideResponse(TideBase):
    pass