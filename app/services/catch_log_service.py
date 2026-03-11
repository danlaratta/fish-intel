from app.crud.catch_log_crud import CatchLogCrud
from app.models.catch_log import CatchLog
from app.schemas.catch_log_schema import CatchLogCreate


class CatchLogService:
    def __init__(self, catch_log_crud: CatchLogCrud) -> None:
        self.catch_log_crud = catch_log_crud


    async def create_catch_log(self, create_data: CatchLogCreate, user_id: int) -> CatchLog:
        catch_log = CatchLog(**create_data.model_dump(), user_id=user_id)
        return await self.catch_log_crud.create_catch_log(catch_log)