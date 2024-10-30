from app.models.user import User
from app.schemas.user import UserCreate
from app.db.session import async_session
from app.exceptions.custom_exceptions import LanguageNotFoundException
from app.utils.reference_data_loader import load_reference_data

reference_data = load_reference_data()


async def create_user(user_in: UserCreate) -> User:
    async with async_session() as session:
        language = user_in.language if user_in.language in reference_data["languages"] else "en"
        currency = reference_data["languages"].get(language, {}).get("currency", "USD")

        async with session.begin():
            user = User(
                tg_id=user_in.tg_id,
                username=user_in.username,
                steam_id=None,
                premium=False,
                language=language,
                currency=currency,
                game="cs2",
            )
            session.add(user)
            await session.flush()
            await session.refresh(user)
            return user
