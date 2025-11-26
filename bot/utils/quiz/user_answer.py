from db import get_session
from sqlalchemy import select

from db.models import UserAnswer


def save_user_anwers():
    with get_session() as db:
        pass
