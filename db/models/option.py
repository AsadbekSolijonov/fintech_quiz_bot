from typing import Optional, TYPE_CHECKING, List

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, ForeignKey, UniqueConstraint, text, Index
from db.base import Base

if TYPE_CHECKING:
    from db.models import Quiz, UserAnswer


class Option(Base):
    __tablename__ = 'options'
    __table_args__ = (
        UniqueConstraint('quiz_id', 'text', name='uq_option_quiz_text'),
        # Faqat Postgres SQLda
        Index(
            'ix_quiz_single_correct',
            'quiz_id',
            unique=True,
            postgresql_where=text('is_correct = TRUE'),
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(256), nullable=False)
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    quiz_id: Mapped[int] = mapped_column(ForeignKey("quizzes.id", ondelete='CASCADE'), nullable=False)

    quiz: Mapped["Quiz"] = relationship(back_populates='options')
    user_answers: Mapped[List["UserAnswer"]] = relationship(
        back_populates='option',
        cascade="all, delete-orphan",
        passive_deletes=True,
        single_parent=True,
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.text[:10]!r}, {self.is_correct})"
