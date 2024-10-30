# app/models/steam_item.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base

class Item(Base):
    __tablename__ = "items"

    id: Mapped[int] = mapped_column(primary_key=True)
    nameid: Mapped[int] = mapped_column(Integer, nullable=False)
    hash_name: Mapped[str] = mapped_column(String, nullable=False)
    game: Mapped[int] = mapped_column(Integer, nullable=False)
