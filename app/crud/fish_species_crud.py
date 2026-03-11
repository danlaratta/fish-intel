from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from app.models.fish_species import FishSpecies

class FishSpeciesCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create fish species
    async def create_fish_species(self) -> None:
        pass


    # Get fish species by id
    async def get_fish_species(self, spot_id: int) -> FishSpecies:
        result = await self.db_session.execute(select(FishSpecies).where(FishSpecies.id == spot_id))
        fish_species: FishSpecies | None = result.scalar_one_or_none()

        if fish_species is None:
            raise DatabaseException(f'No FishSpecies found with id: {spot_id}')
        
        return fish_species


    # Delete fish species
    async def delete_fish_species(self, spot_id: int) -> None:
        pass