from pydantic import BaseModel
from datetime import datetime
from app.enums.user_role import UserRole
from app.enums.subscription_tier import SubscriptionTier


class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserCreate(UserBase):
    pass


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    subscription_tier: SubscriptionTier | None = None
    is_active: bool | None = None


class UserResponse(UserBase):
    id: int
    role: UserRole
    subscription_tier: SubscriptionTier
    is_active: bool
    created_at: datetime
    updated_at: datetime | None

    class Config:
        from_attributes = True