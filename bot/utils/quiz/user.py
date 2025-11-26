from db import get_session
from sqlalchemy import select

from db.models import User


def get_user(chat_id):
    with get_session() as db:
        user = db.scalar(select(User).where(chat_id == User.chat_id))
    return user
