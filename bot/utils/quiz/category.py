from db import get_session
from sqlalchemy import select

from db.models import Category


def get_categories():
    with get_session() as db:
        categories = db.scalars(select(Category)).all()
    return categories
