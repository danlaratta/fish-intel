from sqlalchemy import Integer, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.models.base import Base 
from app.enums.tide import Tide


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
    # fishing_spot_id