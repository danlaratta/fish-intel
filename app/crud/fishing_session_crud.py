from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from app.models.fishing_session import FishingSession

class FishingSessionCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create fishing session
    async def create_fishing_session(self) -> None:
        pass


    # Get fishing session by id
    async def get_fishing_session(self, session_id: int) -> FishingSession:
        result = await self.db_session.execute(select(FishingSession).where(FishingSession.id == session_id))
        fishing_session: FishingSession | None = result.scalar_one_or_none()

        if fishing_session is None:
            raise DatabaseException(f'No FishingSession found with id: {session_id}')
        
        return fishing_session


    # Delete fishing session
    async def delete_fishing_session(self, session_id: int) -> None:
        pass