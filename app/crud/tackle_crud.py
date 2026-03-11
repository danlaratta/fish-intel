from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from app.models.tackle import Tackle

class TackleCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create tackle
    async def create_tackle(self) -> None:
        pass


    # Get tackle by id
    async def get_tackle(self, spot_id: int) -> Tackle:
        result = await self.db_session.execute(select(Tackle).where(Tackle.id == spot_id))
        tackle: Tackle | None = result.scalar_one_or_none()

        if tackle is None:
            raise DatabaseException(f'No Tackle found with id: {spot_id}')
        
        return tackle


    # Delete tackle
    async def delete_tackle(self, spot_id: int) -> None:
        pass