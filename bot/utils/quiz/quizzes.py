from db import get_session
from sqlalchemy import select

from db.models import Quiz


def get_quizzes(sub_id: int):
    with get_session() as db:
        quizzes = db.scalars(select(Quiz).where(sub_id == Quiz.subcategory_id)).all()
    return quizzes


def get_quiz_by_id(quiz_id: int):
    with get_session() as db:
        quiz = db.scalar(select(Quiz).where(quiz_id == Quiz.id))
    return quiz
