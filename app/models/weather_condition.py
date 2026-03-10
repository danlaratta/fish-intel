from sqlalchemy import Float, Integer, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.models.base import Base 

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
    # fishing_spot_id
