from sqlalchemy import Integer, Enum, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.enums.fishing_method import FishingMethod


class FishingSession:
    __tablename__ = 'fishing_sessions'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_start: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    session_end: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False)
    fishing_method: Mapped[FishingMethod] = mapped_column(Enum(
        FishingMethod,
        name = 'fishing_method',
        native_enum = True,
        values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=True)

    # Foreign Keys


    # Relationships
    


