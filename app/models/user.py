from sqlalchemy import Integer, String, Enum, Boolean, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.enums.user_role import UserRole
from app.enums.subscription_tier import SubscriptionTier


class User:
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100), nullable=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    role: Mapped[UserRole] = mapped_column(
        Enum(
            UserRole,
            name='role',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        default=UserRole.MEMBER,
        nullable=False
    )
    subscription_tier: Mapped[SubscriptionTier] = mapped_column(
        Enum(
            SubscriptionTier,
            name='subscription_tier',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        default=SubscriptionTier.FREE,
        nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

    # Relationships