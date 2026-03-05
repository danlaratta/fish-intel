from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class FishSpecies:
    __tablename__ = 'species'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)

    # Relationships
    # session
    # limit
    # catchlog