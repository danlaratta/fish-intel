from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from typing import Any
from app.models.fish_limit import FishLimit


class FishLimitCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    # Create fish limit
    async def create_fish_limit(self, fish_limit: FishLimit) -> FishLimit:
        self.db_session.add(fish_limit)
        await self.db_session.flush()
        await self.db_session.refresh(fish_limit)
        return fish_limit


    # Get fish limit
    async def get_fish_limit(self, limit_id: int) -> FishLimit:
        result = await self.db_session.execute(select(FishLimit).where(FishLimit.id == limit_id))
        fish_limit: FishLimit | None = result.scalar_one_or_none()

        if fish_limit is None:
            raise DatabaseException(f'No FishLimit found with id: {limit_id}')
        return fish_limit
    

    # Get all fish limits
    async def get_all_fish_limits(self) -> list[FishLimit]:
        result = await self.db_session.execute(select(FishLimit))
        fish_limits: list[FishLimit] = list(result.scalars())
        return fish_limits


    # Update fish limit
    async def update_fish_limit(self, fish_limit: FishLimit, update_limit: dict[str, Any]) -> FishLimit:
        for field, value in update_limit.items():
            setattr(fish_limit, field, value)

        await self.db_session.flush()
        await self.db_session.refresh(fish_limit)
        return fish_limit


    # Delete fish limit
    async def delete_fish_limit(self, fish_limit: FishLimit) -> None:
        await self.db_session.delete(fish_limit)

