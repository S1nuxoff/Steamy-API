from sqlalchemy import select
from app.models.user import User
from app.models.favourite import Favourite
from app.db.session import async_session
from typing import List, Optional
from app.exceptions.custom_exceptions import EmptyFavoriteSteamItemsException, GameNotFoundException
from app.utils.reference_data_loader import load_reference_data

reference_data = load_reference_data()


async def get_favorites(user: User, game: Optional[str] = None) -> List[Favourite]:
    async with async_session() as session:
        async with session.begin():
            query = select(Favourite).where(Favourite.user_id == user.tg_id)

            if game is not None:
                game_data = reference_data["games"].get(game)
                if not game_data:
                    raise GameNotFoundException()
                query = query.where(Favourite.game == game)

            result = await session.execute(query)
            favorites = result.scalars().all()

            if not favorites:
                raise EmptyFavoriteSteamItemsException()

            return favorites


