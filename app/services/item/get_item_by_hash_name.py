from typing import Optional
from sqlalchemy.future import select

from app.models.item import Item
from app.db.session import async_session

async def get_item_by_hash_name(hash_name: str) -> Optional[Item]:
    async with async_session() as session:
        result = await session.execute(
            select(Item).where(Item.hash_name == hash_name)
        )
        return result.scalar_one_or_none()
