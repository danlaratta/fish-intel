from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.exceptions.database_exception import DatabaseException
from app.models.user import User

class UserCrud:
    def __init__(self, db_session: AsyncSession) -> None:
        self.db_session = db_session


    # Create user
    async def create_user(self) -> None:
        pass


    # Get user by id
    async def get_user(self, spot_id: int) -> User:
        result = await self.db_session.execute(select(User).where(User.id == spot_id))
        user: User | None = result.scalar_one_or_none()

        if user is None:
            raise DatabaseException(f'No User found with id: {spot_id}')
        
        return user


    # Delete user
    async def delete_user(self, spot_id: int) -> None:
        pass