from sqlalchemy import select

from app.models.user import User
from app.models.favourite import Favourite
from app.schemas.user import UserRemoveFavorite
from app.db.session import async_session
from app.exceptions.custom_exceptions import ItemNotInFavorites

async def remove_favorite(user: User, user_in:UserRemoveFavorite):
    async with async_session() as session:
        async with session.begin():
            existing_favorite = await session.execute(
                select(Favourite)
                .where(Favourite.user_id == user.tg_id)
                .where(Favourite.item == user_in.item)
                .where(Favourite.game == user_in.game)
            )
            existing_favorite = existing_favorite.scalars().first()

            if not existing_favorite:
                raise ItemNotInFavorites()

            await session.delete(existing_favorite)
            await session.commit()
            return existing_favorite
