from sqlalchemy import Integer, Float, String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.enums.region_type import RegionType

class FishLimit:
    __tablename__ = 'fish_limits'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    min_size_inches: Mapped[float | None] = mapped_column(Float, nullable=True)
    max_size_inches: Mapped[float | None] = mapped_column(Float, nullable=True)
    limit_amount: Mapped[int | None] = mapped_column(Integer, nullable=True)
    region: Mapped[str] = mapped_column(String(150), nullable=False, unique=True)
    region_type: Mapped[RegionType] = mapped_column(
        Enum(
            RegionType,
            name='region_type',
            native_enum=True,
            values_callable=lambda enum_cls: [e.value for e in enum_cls]
        ),
        nullable=False,
        default=RegionType.STATEWIDE
    )

    # Foreign Key
    # species_id