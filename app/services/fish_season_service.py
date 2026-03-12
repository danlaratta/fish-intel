from typing import Any
from app.crud.fish_season_crud import FishSeasonCrud
from app.exceptions.bad_request_exception import BadRequestException
from app.models.fish_season import FishSeason
from app.schemas.fish_season_schema import FishSeasonCreate, FishSeasonUpdate

class FishSeasonService:
    def __init__(self, season_crud: FishSeasonCrud) -> None:
        self.season_crud = season_crud 

    # Create fish season
    async def create_fish_season(self, season_create: FishSeasonCreate) -> FishSeason:
        fish_season: FishSeason = FishSeason(**season_create.model_dump())
        return await self.season_crud.create_fish_season(fish_season)


    # Get fish season
    async def get_fish_season(self, season_id: int) -> FishSeason:
        return await self.season_crud.get_fish_season(season_id)


    # Get all fish seasons
    async def get_all_fish_seasons(self) -> list[FishSeason]:
        return await self.season_crud.get_all_fish_seasons()


    # Update fish season
    async def update_fish_season(self, season_id: int, season_update: FishSeasonUpdate) -> FishSeason:
        fish_season: FishSeason = await self.season_crud.get_fish_season(season_id)
        update_season: dict[str, Any] = season_update.model_dump(exclude_unset=True)

        if not update_season:
            raise BadRequestException('Failed to update fish season, no fields provided for update.')
        
        return await self.season_crud.update_fish_season(fish_season, update_season)
        

    # Delete fish season
    async def delete_fish_season(self, season_id: int) -> None:
        fish_season: FishSeason = await self.season_crud.get_fish_season(season_id)
        await self.season_crud.delete_fish_season(fish_season)