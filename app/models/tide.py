from sqlalchemy import Integer, Enum, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import TYPE_CHECKING
from app.models.base import Base 
from app.enums.tide import Tide

if TYPE_CHECKING:
    from app.models.fishing_spot import FishingSpot


class MarineWeatherCondition(Base):
    __tablename__ = 'marine_weather_conditions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    tide: Mapped[Tide] = mapped_column(Enum(
        Tide,
        name = 'tide',
        native_enum = True,
        values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    tide_time: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)


    # Foreign Keys
    fishing_spot_id: Mapped[int] = mapped_column(ForeignKey('fishing_spots.id'), nullable=False)

    # Relationships
    fishing_spot: Mapped[FishingSpot] = relationship(back_populates='tides')
    