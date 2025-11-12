from typing import List, TYPE_CHECKING
from datetime import datetime
from sqlalchemy import Integer, String, DateTime, func, BigInteger
from sqlalchemy.orm import Mapped, mapped_column, relationship
from db.base import Base

if TYPE_CHECKING:
    from db.models import UserAnswer


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    fullname: Mapped[str] = mapped_column(String(100), nullable=False)
    chat_id: Mapped[int] = mapped_column(BigInteger, unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(30), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(),
                                                 onupdate=func.now(), nullable=False)

    answers: Mapped[List["UserAnswer"]] = relationship(
        back_populates='user',
        cascade='all, delete-orphan',
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.chat_id}, {self.fullname!r}, {self.created_at}, {self.updated_at})"
