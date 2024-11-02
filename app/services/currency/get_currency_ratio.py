from sqlalchemy.future import select
from typing import Optional
from app.models.currency import Currency
from app.db.session import async_session

async def get_currency_ratio(name: str) -> Optional[float]:
    async with async_session() as session:
        stmt = select(Currency.ratio).where(Currency.name == name)  # Выбираем только столбец ratio
        result = await session.execute(stmt)
        ratio = result.scalar_one_or_none()
        return ratio
