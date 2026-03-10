from sqlalchemy import Float, Integer, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.models.base import Base 

class MarineWeatherCondition(Base):
    __tablename__ = 'marine_weather_conditions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    water_temp: Mapped[float] = mapped_column(Float, nullable=False)
    wave_height: Mapped[float] = mapped_column(Float, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())

    # Foreign Keys
    # fishing_spot_id
