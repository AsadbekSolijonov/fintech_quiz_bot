from typing import List, TYPE_CHECKING
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, CheckConstraint, UniqueConstraint
from db.base import Base

if TYPE_CHECKING:
    from db.models import Category, Quiz


class Subcategory(Base):
    __tablename__ = 'subcategories'
    __table_args__ = (
        CheckConstraint("char_length(btrim(name)) > 2", name="check_subcat_name_gt_two"),
        UniqueConstraint('category_id', 'name', name='uq_subcategory_cat_name'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id", ondelete='CASCADE'), nullable=False)

    category: Mapped["Category"] = relationship(back_populates='subcategories')
    quizzes: Mapped[List["Quiz"]] = relationship(
        back_populates='subcategory',
        cascade='all, delete-orphan',
        passive_deletes=True,
        single_parent=True,
    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name!r})"
