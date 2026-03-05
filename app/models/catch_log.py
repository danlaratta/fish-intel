from sqlalchemy import Integer, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column


class CatchLog:
    __tablename__ = 'catch_logs'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    length: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)   # In inches
    weight: Mapped[float] = mapped_column(Float, nullable=True)
    released: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    # Foreign Keys
    
