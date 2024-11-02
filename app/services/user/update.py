from app.models.user import User
from app.schemas.user import UserUpdate
from app.db.session import async_session

from app.utils.reference_data_loader import load_reference_data
reference_data = load_reference_data()

async def update(user: User, user_in: UserUpdate) -> User:
    async with async_session() as session:
        async with session.begin():

            if user_in.username is not None:
                user.username = user_in.username

            if user_in.steam_id is not None:
                user.steam_id = user_in.steam_id

            if user_in.premium is not None:
                user.premium = user_in.premium

            merged_user = await session.merge(user)
            await session.flush()
            await session.refresh(merged_user)
            return merged_user
