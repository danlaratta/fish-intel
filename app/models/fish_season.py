from sqlalchemy import ForeignKey, Integer, Date, Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from typing import TYPE_CHECKING
from app.models.base import Base 
from app.enums.region_type import RegionType

if TYPE_CHECKING:
    from app.models.fish_species import FishSpecies

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
    species_id: Mapped[int] = mapped_column(ForeignKey('species.id'), nullable=False)

    # Relationships
    fish_species: Mapped[FishSpecies] = relationship(back_populates='fish_seasons')

