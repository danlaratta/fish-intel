from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import Any
from app.exceptions.database_exception import DatabaseException
from app.models.fishing_session import FishingSession

class FishingSessionCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create fishing session
    async def create_fishing_session(self, session: FishingSession) -> FishingSession:
        self.db_session.add(session)
        await self.db_session.flush()
        await self.db_session.refresh(session)
        return session


    # Get fishing session
    async def get_fishing_session(self, session_id: int) -> FishingSession:
        result = await self.db_session.execute(select(FishingSession).where(FishingSession.id == session_id))
        fishing_session: FishingSession | None = result.scalar_one_or_none()

        if fishing_session is None:
            raise DatabaseException(f'No FishingSession found with id: {session_id}')
        
        return fishing_session
    

    # Get all fishing sessions
    async def get_all_fishing_sessions(self) -> list[FishingSession]:
        result = await self.db_session.execute(select(FishingSession))
        fishing_session: list[FishingSession] = list(result.scalars())
        return fishing_session


    # Update fishing session
    async def update_fishing_session(self, session: FishingSession, update_session: dict[str, Any]) -> FishingSession:
        for field, value in update_session.items():
            setattr(FishingSession, field, value)

        await self.db_session.flush()
        await self.db_session.refresh(session)
        return session

    # Delete fishing session
    async def delete_fishing_session(self, session: FishingSession) -> None:
        await self.db_session.delete(session)