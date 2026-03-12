from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Any
from app.exceptions.database_exception import DatabaseException
from app.models.fish_season import FishSeason

class FishSeasonCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session

    # Create fish season
    async def create_fish_season(self, fish_season: FishSeason) -> FishSeason:
        self.db_session.add(fish_season)
        await self.db_session.flush()
        await self.db_session.refresh(fish_season)
        return fish_season


    # Get fish season
    async def get_fish_season(self, season_id: int) -> FishSeason:
        result = await self.db_session.execute(select(FishSeason).where(FishSeason.id == season_id))
        fish_season: FishSeason | None = result.scalar_one_or_none()

        if fish_season is None:
            raise DatabaseException(f'No CatchLog found with id: {season_id}')
        
        return fish_season


    # Get all fish seasons
    async def get_all_fish_seasons(self) -> list[FishSeason]:
        result = await self.db_session.execute(select(FishSeason))
        fish_seasons: list[FishSeason] = list(result.scalars())
        return fish_seasons


    # Update fish season
    async def update_fish_season(self, fish_season: FishSeason, update_season: dict[str, Any]) -> FishSeason:
        for field, value in update_season.items():
            setattr(FishSeason, field, value)

        await self.db_session.flush()
        await self.db_session.refresh(fish_season)
        return fish_season


    # Delete fish season
    async def delete_fish_season(self, fish_season: FishSeason) -> None:
        await self.db_session.delete(fish_season)


