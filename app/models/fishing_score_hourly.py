from sqlalchemy import Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.models.base import Base 

class FishingScoreHourly(Base):
    __tablename__ = 'hourly_scores'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    hour: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    score_points: Mapped[int] = mapped_column(Integer, nullable=False)
    
    # Foreign Keys
    # fishing_spot_id: Mapped[int] = mapped_column(ForeignKey("fishing_spots.id"), nullable=False)