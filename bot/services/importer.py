from sqlalchemy import select
from db.models import Category, Subcategory, Quiz, Option
import pandas as pd

from db import get_session


def import_excel_to_database(excel_file_path):
    df = pd.read_excel(excel_file_path, sheet_name='quizzes')
    with get_session() as db:
        for idx, row in df.iterrows():
            excel_row = idx + 2

            category_name = row.get('Category')
            subcategory_name = row.get('Subcategory')
            quiz_text = row.get('Quiz')

            a_text = row.get('A_true')
            b_text = row.get('B')
            c_text = row.get('C')
            d_text = row.get('D')

            option_values = [
                (a_text, True),
                (b_text, False),
                (c_text, False),
                (d_text, False),
            ]

            options = [(text, is_correct) for text, is_correct in option_values if text]

            if not (category_name and subcategory_name and quiz_text):
                raise ValueError("Error: Category/Subcategory/Quiz text is empty")

            if len(options) < 2:
                raise ValueError("Error: Variant kamida 2 ta yoki ko'pi bilan 4 ta bo'lishi mumkin.")

            category = db.scalar(select(Category).where(category_name == Category.name))
            if category is None:
                category = Category(name=category_name)
                db.add(category)
                db.flush()

            subcategory = db.scalar(
                select(Subcategory).where(
                    subcategory_name == Subcategory.name,
                    category.id == Subcategory.category_id)
            )

            if subcategory is None:
                subcategory = Subcategory(name=subcategory_name, category_id=category.id)
                db.add(subcategory)
                db.flush()

            # quiz
            quiz = db.scalar(select(Quiz).where(Quiz.text == quiz_text, subcategory.id == Quiz.subcategory_id))
            if quiz is None:
                quiz = Quiz(text=quiz_text, subcategory_id=subcategory.id)
                db.add(quiz)
                db.flush()

            # option
            for text, is_correct in options:
                option = db.scalar(select(Option).where(text == Option.text, quiz.id == Option.quiz_id))
                if option is None:
                    option = Option(text=text, is_correct=is_correct, quiz_id=quiz.id)
                    db.add(option)

        db.commit()
