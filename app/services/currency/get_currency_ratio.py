from typing import Optional

from sqlalchemy.future import select

from app.schemas.currency import Currency
from app.db.session import async_session

async def get_currency_ratio(tg_id: int) -> Optional[User]:
    async with async_session() as session:
        result = await session.execute(
            select(User).where(User.tg_id == tg_id)
        )
        return result.scalar_one_or_none()