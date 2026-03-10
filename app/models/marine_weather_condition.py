from sqlalchemy import Float, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.fishing_spot import FishingSpot

class MarineWeatherCondition(Base):
    __tablename__ = 'marine_weather_conditions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    water_temp: Mapped[float] = mapped_column(Float, nullable=False)
    wave_height: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    # Foreign Keys
    fishing_spot_id: Mapped[int] = mapped_column(ForeignKey('fishing_spots.id'), nullable=False)

    # Relationships
    fishing_spot: Mapped[FishingSpot] = relationship(back_populates='marine_weather_conditions')
    