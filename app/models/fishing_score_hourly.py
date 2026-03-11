from sqlalchemy import ForeignKey, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.models.base import Base 

if TYPE_CHECKING:
    from app.models.fishing_spot import FishingSpot


class FishingScoreHourly(Base):
    __tablename__ = 'hourly_scores'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hour: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    score: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # Foreign Keys
    fishing_spot_id: Mapped[int] = mapped_column(ForeignKey('fishing_spots.id'), nullable=False)

    # Relationships
    fishing_spot: Mapped[FishingSpot] = relationship(back_populates='hourly_scores')
