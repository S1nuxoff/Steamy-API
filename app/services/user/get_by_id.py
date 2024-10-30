from typing import Optional

from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from app.models.user import User
from app.db.session import async_session

async def get_user_by_id(tg_id: int) -> Optional[User]:
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.tg_id == tg_id)
        )
        return result.scalar_one_or_none()