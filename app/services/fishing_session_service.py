from typing import Any
from app.crud.fishing_session_crud import FishingSessionCrud
from app.exceptions.bad_request_exception import BadRequestException
from app.models.fishing_session import FishingSession
from app.schemas.fishing_session_schema import FishingSessionCreate, FishingSessionUpdate

class FishingSessionService:
    def __init__(self, session_crud: FishingSessionCrud) -> None:
        self.session_crud = session_crud 


    # Create fishing session
    async def create_fishing_session(self, session_create: FishingSessionCreate) -> FishingSession:
        session: FishingSession = FishingSession(**session_create.model_dump())
        return await self.session_crud.create_fishing_session(session)


    # Get fishing session
    async def get_fishing_session(self, session_id: int) -> FishingSession:
        return await self.session_crud.get_fishing_session(session_id)


    # Get all fishing sessions
    async def get_all_fishing_sessions(self) -> list[FishingSession]:
        return await self.session_crud.get_all_fishing_sessions()
    

    # Update fishing session
    async def update_fishing_session(self, session_id: int, session_update: FishingSessionUpdate) -> FishingSession:
        session: FishingSession = await self.session_crud.get_fishing_session(session_id)
        update_session: dict[str, Any] = session_update.model_dump(exclude_unset=True)

        if not update_session:
            raise BadRequestException('Failed to update fishing session, no fields provided for update.')

        return await self.session_crud.update_fishing_session(session, update_session)


    # Delete fishing session
    async def delete_fishing_session(self, session_id: int) -> None:
        session: FishingSession = await self.session_crud.get_fishing_session(session_id)
        await self.session_crud.delete_fishing_session(session)