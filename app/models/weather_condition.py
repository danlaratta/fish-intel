from sqlalchemy import Float, Integer, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.fishing_spot import FishingSpot

class WeatherCondition(Base):
    __tablename__ = 'weather_conditions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    wind_speed: Mapped[int] = mapped_column(Integer, nullable=False)
    wind_direction_degrees: Mapped[float] = mapped_column(Float, nullable=False)
    air_temp: Mapped[int] = mapped_column(Integer, nullable=False)
    air_pressure: Mapped[float] = mapped_column(Float, nullable=False)
    weather_code: Mapped[int] = mapped_column(Integer, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    # Foreign Keys
    fishing_spot_id: Mapped[int] = mapped_column(ForeignKey('fishing_spots.id'), nullable=False)

    # Relationships
    fishing_spot: Mapped[FishingSpot] = relationship(back_populates='fishing_sessions')
