from typing import List, Optional, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, CheckConstraint, UniqueConstraint
from db.base import Base
if TYPE_CHECKING:
    from db.models import Subcategory, Option, UserAnswer


class Quiz(Base):
    __tablename__ = 'quizzes'
    __table_args__ = (
        CheckConstraint("length(text) > 2", name="check_quiz_text_gt_two"),
        UniqueConstraint('subcategory_id', 'text', name="uq_sub_id__sub_text")
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    text: Mapped[str] = mapped_column(String(500), nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    subcategory_id: Mapped[int] = mapped_column(ForeignKey("subcategories.id", ondelete='CASCADE'), nullable=False)

    subcategory: Mapped["Subcategory"] = relationship(back_populates='quizzes')
    options: Mapped[List["Option"]] = relationship(back_populates='quiz', cascade='all, delete-orphan')
    user_answers: Mapped[List["UserAnswer"]] = relationship(
        back_populates='quiz',
        cascade="all, delete-orphan",
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.text[:10]!r})"
