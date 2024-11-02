from app.models.user import User
from app.schemas.user import UserCreate
from app.db.session import async_session
from app.utils.reference_data_loader import load_reference_data

reference_data = load_reference_data()


async def create_user(user_in: UserCreate) -> User:
    async with async_session() as session:
        async with session.begin():
            user = User(
                tg_id=user_in.tg_id,
                username=user_in.username,
                steam_id=None,
                premium=False,
            )
            session.add(user)
            await session.flush()
            await session.refresh(user)
            return user
