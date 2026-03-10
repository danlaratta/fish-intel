from pydantic import BaseModel


class UserBase(BaseModel):
    pass 


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserResponse(UserBase):
    pass