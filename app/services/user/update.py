from app.models.user import User
from app.schemas.user import UserUpdate
from app.db.session import async_session

from app.exceptions.custom_exceptions import LanguageNotFoundException, CurrencyNotFoundException, GameNotFoundException
from app.utils.reference_data_loader import load_reference_data
reference_data = load_reference_data()

async def update(user: User, user_in: UserUpdate) -> User:
    async with async_session() as session:
        async with session.begin():

            if user_in.username is not None:
                user.username = user_in.username

            if user_in.steam_id is not None:
                user.steam_id = user_in.steam_id

            if user_in.language is not None:
                if user_in.language not in reference_data["languages"]:
                    raise LanguageNotFoundException()
                user.language = user_in.language  # Или присвоение ID/кода

            if user_in.currency is not None:
                if user_in.currency not in reference_data["currencies"]:
                    raise CurrencyNotFoundException()
                user.currency = user_in.currency  # Или присвоение кода валюты

            if user_in.game is not None:
                if user_in.game not in reference_data["games"]:
                    raise GameNotFoundException()
                user.game = user_in.game

            merged_user = await session.merge(user)
            await session.flush()
            await session.refresh(merged_user)
            return merged_user
