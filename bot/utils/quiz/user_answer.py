from db import get_session
from sqlalchemy import select

from db.models import UserAnswer


def save_user_answer(user_id, quiz_id, option_id):
    with get_session() as db:
        ua = UserAnswer(user_id=user_id, quiz_id=quiz_id, option_id=option_id)
        db.add(ua)
        db.commit()
        db.refresh(ua)
    return bool(ua)

