from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.fish_season import FishSeason
    from app.models.fish_limit import FishLimit
    from app.models.catch_log import CatchLog

class FishSpecies(Base):
    __tablename__ = 'species'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    # Relationships
    fish_seasons: Mapped[list[FishSeason]] = relationship(back_populates='fish_species', cascade='all, delete-orphan')
    fish_limits: Mapped[list[FishLimit]] = relationship(back_populates='fish_species', cascade='all, delete-orphan')
    catch_logs: Mapped[list[CatchLog]] = relationship(back_populates='fish_species', cascade='all, delete-orphan')