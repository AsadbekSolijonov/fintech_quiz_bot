from typing import TYPE_CHECKING
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey, DateTime, func, UniqueConstraint
from db.base import Base

if TYPE_CHECKING:
    from db.models import User, Quiz, Option


class UserAnswer(Base):
    __tablename__ = 'user_answers'
    __table_args__ = (
        UniqueConstraint("user_id", "quiz_id", name="uq_user_quiz"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete='CASCADE'), nullable=False)
    quiz_id: Mapped[int] = mapped_column(ForeignKey("quizzes.id", ondelete='CASCADE'), nullable=False)
    option_id: Mapped[int] = mapped_column(ForeignKey("options.id", ondelete='CASCADE'), nullable=False)
    answered_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    user: Mapped["User"] = relationship(back_populates='answers')
    quiz: Mapped["Quiz"] = relationship(back_populates='user_answers')
    option: Mapped["Option"] = relationship(back_populates='user_answers')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id})"
