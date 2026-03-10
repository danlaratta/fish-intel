from sqlalchemy import Integer, Float, String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base 

class FishingSpot(Base):
    __tablename__ = 'fishing_spots'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False, unique=True)
    longitude: Mapped[float] = mapped_column(Float, nullable=False)
    latitude: Mapped[float] = mapped_column(Float, nullable=False)

    # Foreign Key
    # user_id

    # Relationships
    # session
    # condition