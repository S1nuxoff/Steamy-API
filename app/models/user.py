
from sqlalchemy import BigInteger, JSON, Boolean, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, nullable=False)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True, nullable=False)
    steam_id: Mapped[Optional[int]] = mapped_column(Integer, unique=True, nullable=True)
    premium: Mapped[bool] = mapped_column(Boolean, default=False)
    language: Mapped[str] = mapped_column(String, nullable=False)
    currency: Mapped[str] = mapped_column(String, nullable=False)
    game: Mapped[str] = mapped_column(String, nullable=False)
    favourites = relationship("Favourite", back_populates="user", cascade="all, delete-orphan")