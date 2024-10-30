from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.sql import func
from app.models.base import Base

class Currency(Base):
    __tablename__ = "currencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    ratio: Mapped[float] = mapped_column(Float, nullable=False)
    time: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
