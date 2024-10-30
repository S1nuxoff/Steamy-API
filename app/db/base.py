# app/db/base.py
from app.db.session import engine
from app.models.base import Base  # Base declarative class

async def create_all_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
