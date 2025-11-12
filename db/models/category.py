from typing import List, TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, CheckConstraint
from db.base import Base

if TYPE_CHECKING:
    from db.models import Subcategory


class Category(Base):
    __tablename__ = 'categories'
    __table_args__ = (
        CheckConstraint("length(name) > 2", name="check_cat_name_gt_two"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    subcategories: Mapped[List["Subcategory"]] = relationship(
        back_populates='category',
        cascade='all, delete-orphan',
        passive_deletes=True,

    )

    def __repr__(self):
        return f"{self.__class__.__name__}({self.id}, {self.name!r})"
