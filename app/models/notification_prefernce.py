from sqlalchemy import Float, Integer, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base 

class NotificationSettings(Base):
    __tablename__ = 'notification_settings'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    score_alert_threshold: Mapped[float] = mapped_column(Float, nullable=False)
    email_notifications_enabled: Mapped[bool] = mapped_column(Boolean, default=True)

    # Foreign Keys
    # user_id