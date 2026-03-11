from pydantic import BaseModel
from datetime import datetime
from app.enums.user_role import UserRole
from app.enums.subscription_tier import SubscriptionTier


class UserBase(BaseModel):
    first_name: str 
    last_name: str 
    email: str
    role: UserRole = UserRole.MEMBER
    subscription_tier: SubscriptionTier = SubscriptionTier.FREE
    is_active: bool = True 
    updated_at: datetime | None 

class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    subscription_tier: SubscriptionTier = SubscriptionTier.FREE
    is_active: bool = True 
    updated_at: datetime | None


class UserResponse(UserBase):
    id: int 
    created_at: datetime

    class Config:
        from_attributes = True