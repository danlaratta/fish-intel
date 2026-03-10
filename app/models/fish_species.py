from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base 

class FishSpecies(Base):
    __tablename__ = 'species'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    # Relationships
    # season
    # limit
    # catchlog