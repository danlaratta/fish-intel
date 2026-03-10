from sqlalchemy import Float, ForeignKey, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.user import User

class NotificationSettings(Base):
    __tablename__ = 'notification_settings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    score_alert_threshold: Mapped[float] = mapped_column(Float, nullable=False)
    email_notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False, unique=True)

    # Relationships
    user: Mapped['User'] = relationship(back_populates='notification_settings')
    