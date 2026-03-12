from app.crud.fish_species_crud import FishSpeciesCrud
from app.models.fish_species import FishSpecies
from app.schemas.fish_species_schema import FishSpeciesCreate


class FishSpeciesService:
    def __init__(self, species_crud: FishSpeciesCrud) -> None:
        self.species_crud = species_crud


    # Create fish species
    async def create_fish_species(self, species_create: FishSpeciesCreate) -> FishSpecies:
        fish_species: FishSpecies = FishSpecies(**species_create.model_dump())
        return await self.species_crud.create_fish_species(fish_species)


    # Get fish species
    async def get_fish_species(self, species_id: int) -> FishSpecies:
        return await self.species_crud.get_fish_species(species_id)


    # Get all fish speciess
    async def get_all_fish_speciess(self) -> list[FishSpecies]:
        return await self.species_crud.get_all_fish_species()


    # Delete fish species
    async def delete_fish_species(self, species_id: int) -> None:
        fish_species: FishSpecies = await self.species_crud.get_fish_species(species_id)
        await self.species_crud.delete_fish_species(fish_species)