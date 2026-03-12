from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from app.models.catch_log import CatchLog

class CatchLogCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create catch log
    async def create_catch_log(self, catch_log: CatchLog) -> CatchLog:
        self.db_session.add(catch_log)
        await self.db_session.flush()
        await self.db_session.refresh(catch_log)
        return catch_log


    # Get catch log by id
    async def get_catch_log(self, log_id: int, user_id: int) -> CatchLog:
        result = await self.db_session.execute(select(CatchLog).where(CatchLog.id == log_id).where(CatchLog.user_id == user_id))
        catch_log: CatchLog | None = result.scalar_one_or_none()

        if catch_log is None:
            raise DatabaseException(f'No CatchLog found with id: {log_id}')
        
        return catch_log


    # Delete catch log
    async def delete_catch_log(self, catch_log: CatchLog) -> None:
        await self.db_session.delete(catch_log)



