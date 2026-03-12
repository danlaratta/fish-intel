from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from app.models.fish_species import FishSpecies

class FishSpeciesCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create fish species
    async def create_fish_species(self, fish_species: FishSpecies) -> FishSpecies:
        self.db_session.add(fish_species)
        await self.db_session.flush()
        await self.db_session.refresh(fish_species)
        return fish_species


    # Get fish species
    async def get_fish_species(self, species_id: int) -> FishSpecies:
        result = await self.db_session.execute(select(FishSpecies).where(FishSpecies.id == species_id))
        fish_species: FishSpecies | None = result.scalar_one_or_none()

        if fish_species is None:
            raise DatabaseException(f'No FishSpecies found with id: {species_id}')
        
        return fish_species


    # Get fish species
    async def get_all_fish_species(self) -> list[FishSpecies]:
        result = await self.db_session.execute(select(FishSpecies))
        fish_species: list[FishSpecies] = list(result.scalars())
        return fish_species
    

    # Delete fish species
    async def delete_fish_species(self, fish_species: FishSpecies) -> None:
        await self.db_session.delete(fish_species)