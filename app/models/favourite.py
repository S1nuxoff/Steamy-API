from sqlalchemy import ForeignKey, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.models.base import Base

class Favourite(Base):
    __tablename__ = "favourites"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.tg_id"), nullable=False)
    item: Mapped[str] = mapped_column(String, nullable=False)  # Название предмета
    game: Mapped[str] = mapped_column(String, nullable=False)  # Название игры
    added_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)  # Время добавления в избранное
    user: Mapped["User"] = relationship("User", back_populates="favourites")