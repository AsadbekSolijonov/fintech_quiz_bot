from db import get_session
from sqlalchemy import select

from db.models import Subcategory


def get_subcategories(cat_id: int):
    with get_session() as db:
        sub_categories = db.scalars(select(Subcategory).where(cat_id == Subcategory.category_id)).all()
    return sub_categories
