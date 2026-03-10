from sqlalchemy import Integer, Date, Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from app.models.base import Base 
from app.enums.region_type import RegionType

class FishSeason(Base):
    __tablename__ = 'fish_seasons'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    season_start: Mapped[date | None] = mapped_column(Date, nullable=True)
    season_end: Mapped[date | None] = mapped_column(Date, nullable=True)
    region: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    region_type: Mapped[RegionType] = mapped_column(
        Enum(
            RegionType,
            name='region_type',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False,
        default=RegionType.STATEWIDE
    )

    # Foreign Key
    # species_id

