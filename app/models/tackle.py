from sqlalchemy import Integer, Enum, String
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base 
from app.enums.lure_type import LureType
from app.enums.tackle_type import TackleType

class Tackle(Base):
    __tablename__ = 'tackle'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    tackle_type: Mapped[TackleType] = mapped_column(Enum(
        TackleType,
        name = 'tackle_type',
        native_enum = True,
        values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False
    )
    lure_type: Mapped[LureType | None] = mapped_column(Enum(
        LureType,
        name = 'lure_type',
        native_enum = True,
        values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=True
    )
    color: Mapped[str | None] = mapped_column(String(100), nullable=True)
    lure_size: Mapped[str | None] = mapped_column(String(100), nullable=True)
    jig_head_size: Mapped[str | None] = mapped_column(String(100), nullable=True)

    # Relationship
    # catch log one to one
    