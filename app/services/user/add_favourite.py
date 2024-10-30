from datetime import datetime
from sqlalchemy import select
from app.models.user import User
from app.models.favourite import Favourite
from app.schemas.user import UserAddFavorite
from app.db.session import async_session
from app.exceptions.custom_exceptions import ItemAlreadyInFavorites
from app.utils.reference_data_loader import load_reference_data
from app.exceptions.custom_exceptions import GameNotFoundException

reference_data = load_reference_data()



async def add_favorite(user: User, user_in: UserAddFavorite) -> Favourite:
    async with async_session() as session:
        game_data = reference_data["games"].get(user_in.game)
        if not game_data:
            raise GameNotFoundException()
        async with session.begin():
            existing_favorite = await session.execute(
                select(Favourite)
                .where(Favourite.user_id == user.tg_id)
                .where(Favourite.item == user_in.item)
                .where(Favourite.game == user_in.game)
            )
            existing_favorite = existing_favorite.scalars().first()
            if existing_favorite:
                raise ItemAlreadyInFavorites

            new_favorite = Favourite(
                user_id=user.tg_id,
                item=user_in.item,
                game=user_in.game,
                added_at=datetime.utcnow()
            )
            session.add(new_favorite)
            await session.commit()
            return new_favorite
