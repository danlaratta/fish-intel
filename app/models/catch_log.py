from sqlalchemy import Integer, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class CatchLog:
    __tablename__ = 'catch_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    length_inches: Mapped[float] = mapped_column(Float, nullable=False, default=0.0) 
    weight_lb: Mapped[float | None] = mapped_column(Float, nullable=True)
    released: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Foreign Keys
    # fishing_session_id
    # species_id
    # tackle_id
