from typing import Any
from app.crud.fish_limit_crud import FishLimitCrud
from app.exceptions.bad_request_exception import BadRequestException
from app.models.fish_limit import FishLimit
from app.schemas.fish_limit_schema import FishLimitCreate, FishLimitUpdate


class FishLimitService:
    def __init__(self, limit_crud: FishLimitCrud) -> None:
        self.limit_crud = limit_crud


    # Create fish limit
    async def create_fish_limit(self, limit_create: FishLimitCreate) -> FishLimit:
        fish_limit: FishLimit = FishLimit(**limit_create.model_dump())
        return await self.limit_crud.create_fish_limit(fish_limit)


    # Get fish limit
    async def get_fish_limit(self, limit_id: int) -> FishLimit:
        return await self.limit_crud.get_fish_limit(limit_id)


    # Get all fish limits
    async def get_allfish_limits(self) -> list[FishLimit]:
        return await self.limit_crud.get_all_fish_limits()


    # Update fish limit
    async def update_fish_limit(self, limit_id: int, limit_update: FishLimitUpdate) -> FishLimit:
        fish_limit: FishLimit = await self.limit_crud.get_fish_limit(limit_id)
        update_limit: dict[str, Any] = limit_update.model_dump(exclude_unset=True)  # exclude_unset=True --> Returns only fields being updated an provided in the request
        
        if not update_limit:
            raise BadRequestException('Failed to update fish limit, no fields provided for update.')

        return await self.limit_crud.update_fish_limit(fish_limit, update_limit)


    # Delete fish limit
    async def delete_fish_limit(self, limit_id: int) -> None:
        fish_limit: FishLimit = await self.limit_crud.get_fish_limit(limit_id)
        await self.limit_crud.delete_fish_limit(fish_limit)

