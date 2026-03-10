from sqlalchemy import Integer, Float, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING
from app.models.base import Base

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.fishing_session import FishingSession
    from app.models.fish_species import FishSpecies
    from app.models.tackle import Tackle
    from app.models.fishing_spot import FishingSpot

class CatchLog(Base):
    __tablename__ = 'catch_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    length_inches: Mapped[float] = mapped_column(Float, nullable=False) 
    weight_lb: Mapped[float | None] = mapped_column(Float, nullable=True)
    released: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Foreign Keys
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    fishing_session_id: Mapped[int] = mapped_column(ForeignKey('fishing_sessions.id'), nullable=False)
    species_id: Mapped[int] = mapped_column(ForeignKey('species.id'), nullable=False)
    tackle_id: Mapped[int] = mapped_column(ForeignKey('tackle.id'), nullable=False)
    fishing_spot_id: Mapped[int] = mapped_column(ForeignKey('fishing_spots.id'), nullable=False)

    # Relationships
    user: Mapped[User] = relationship(back_populates='catch_logs')
    fishing_session: Mapped[FishingSession] = relationship(back_populates='catch_logs')
    fish_species: Mapped[FishSpecies] = relationship(back_populates='catch_logs')
    tackle: Mapped[Tackle] = relationship(back_populates='catch_logs')
    fishing_spot: Mapped[FishingSpot] = relationship(back_populates='catch_logs')
    