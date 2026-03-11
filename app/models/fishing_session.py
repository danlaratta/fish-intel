from sqlalchemy import ForeignKey, Integer, Enum, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.models.base import Base 
from app.enums.fishing_method import FishingMethod


if TYPE_CHECKING:
    from app.models.user import User
    from app.models.fishing_spot import FishingSpot
    from app.models.catch_log import CatchLog

class FishingSession(Base):
    __tablename__ = 'fishing_sessions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_start: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    session_end: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    fishing_method: Mapped[FishingMethod] = mapped_column(Enum(
        FishingMethod,
        name = 'fishing_method',
        native_enum = True,
        values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    fishing_spot_id: Mapped[int] = mapped_column(ForeignKey('fishing_spots.id'), nullable=False)

    # Relationships
    user: Mapped[User] = relationship(back_populates='fishing_sessions')
    fishing_spot: Mapped[FishingSpot] = relationship(back_populates='fishing_sessions')
    catch_logs: Mapped[list[CatchLog]] = relationship(back_populates='fishing_session', cascade='all,')


