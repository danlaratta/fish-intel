from sqlalchemy import ForeignKey, Integer, Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.models.base import Base 

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.fishing_session import FishingSession
    from app.models.weather_condition import WeatherCondition
    from app.models.marine_weather_condition import MarineWeatherCondition
    from app.models.tide import Tide
    from app.models.catch_log import CatchLog
    from app.models.fishing_score_hourly import FishingScoreHourly

class FishingSpot(Base):
    __tablename__ = 'fishing_spots'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)

    # Foreign Key
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    # Relationships
    user: Mapped[User] = relationship(back_populates='fishing_spots')
    fishing_sessions: Mapped[list[FishingSession]] = relationship(back_populates='fishing_spot', cascade='all, delete-orphan')
    weather_conditions: Mapped[list[WeatherCondition]] = relationship(back_populates='fishing_spot', cascade='all, delete-orphan')
    marine_weather_conditions: Mapped[list[MarineWeatherCondition]] = relationship(back_populates='fishing_spot', cascade='all, delete-orphan')
    tides: Mapped[list[Tide]] = relationship(back_populates='fishing_spot', cascade='all, delete-orphan')
    catch_logs: Mapped[list[CatchLog]] = relationship(back_populates='fishing_spot', cascade='all, delete-orphan')
    hourly_scores: Mapped[list[FishingScoreHourly]] = relationship(back_populates='fishing_spot', cascade='all, delete-orphan')