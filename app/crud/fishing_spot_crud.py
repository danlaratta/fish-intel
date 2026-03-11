from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from app.models.fishing_spot import FishingSpot

class FishingSpotCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create fishing spot
    async def create_fishing_spot(self) -> None:
        pass


    # Get fishing spot by id
    async def get_fishing_spot(self, spot_id: int) -> FishingSpot:
        result = await self.db_session.execute(select(FishingSpot).where(FishingSpot.id == spot_id))
        fishing_spot: FishingSpot | None = result.scalar_one_or_none()

        if fishing_spot is None:
            raise DatabaseException(f'No FishingSpot found with id: {spot_id}')
        
        return fishing_spot


    # Delete fishing spot
    async def delete_fishing_spot(self, spot_id: int) -> None:
        pass