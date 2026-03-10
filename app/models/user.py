from sqlalchemy import Integer, String, Enum, Boolean, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.models.base import Base 
from app.enums.user_role import UserRole
from app.enums.subscription_tier import SubscriptionTier


if TYPE_CHECKING:
    from app.models.fishing_session import FishingSession
    from app.models.fishing_spot import FishingSpot
    from app.models.catch_log import CatchLog
    from app.models.notification_settings import NotificationSettings

class User(Base):
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
        nullable=False,
        default=UserRole.MEMBER
    )
    subscription_tier: Mapped[SubscriptionTier] = mapped_column(
        Enum(
            SubscriptionTier,
            name='subscription_tier',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False,
        default=SubscriptionTier.FREE
    )
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

    # Relationship
    fishing_sessions: Mapped[list[FishingSession]] = relationship(back_populates='user', cascade='all, delete-orphan')
    fishing_spots: Mapped[list[FishingSpot]] = relationship(back_populates='user', cascade='all, delete-orphan')
    catch_logs: Mapped[list[CatchLog]] = relationship(back_populates='user', cascade='all, delete-orphan')
    notification_settings: Mapped[NotificationSettings] = relationship(back_populates='user', cascade='all, delete-orphan', uselist=False)