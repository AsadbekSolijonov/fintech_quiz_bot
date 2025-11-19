import logging
import math
import os

import pandas as pd
from bot.config import BASE_DIR
from db import get_session
from db.models import Category, Subcategory, Quiz, Option
from sqlalchemy import select

logger = logging.getLogger(__name__)

# [x] Oddiy dict data
# data = {
#     "Ismlar": ["Ali", "Vali", "Eshmat"],
#     "Yoshlar": [34, 24, 23],
#     "Daraja": ["Magister", "Bakalavr", "Bakalavr"]
# }

# [x] pandas DataFrame
# df = pd.DataFrame(data)
# print(df)

# [x] Excel Write
# EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/students.xlsx')
# df.to_excel(EXCEL_FILE_PATH)


# [x] Excel Read
# EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/students.xlsx')
# df = pd.read_excel(EXCEL_FILE_PATH)
# print(df)
# print(df[df['Yoshlar'] >= 24])


# [x] Excel create sheet_name
EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/school.xlsx')
#
# d1 = {
#     "Category": ["Math", "Math", "English", "English"],
#     "Subcategory": ["1-class", "2-class", "2-class", "3-class"],
#     "Quiz": ["2 + 2 =?", "2 * 2 = ?", "My name ... John.", "... is your name?"],
#     "A_true": ["4", "4", "is", "What"],
#     "B": ["5", "8", "are", "Where"],
#     "C": ["2", "1", "or", "When"],
#     "D": ["22", "5", "no", "Why"],
# }
#
# d2 = {
#     "Name": ["Alex", "Bob", "John"],
#     "Age": [7, 8, 9],
# }
#
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
#
# with pd.ExcelWriter(EXCEL_FILE_PATH, engine='openpyxl') as writer:
#     df1.to_excel(writer, sheet_name='quizzes', index=False)
#     df2.to_excel(writer, sheet_name='students', index=False)


# from sqlalchemy.exc import SQLAlchemyError
#
#
# def _clean_str(value):
#     if value is None or (isinstance(value, float) and math.isnan(value)):
#         return None
#     s = str(value).strip()
#     return s or None
#
#
# # [x] sheet_name dan ma'lumot o'qish
# def import_excel_to_db():
#     EXCEL_FILE_PATH = os.path.join(BASE_DIR, 'bot/xlsx/data/school.xlsx')
#     df = pd.read_excel(EXCEL_FILE_PATH, sheet_name='quizzes')
#     category_cache: dict[str, Category] = dict()
#     subcategory_cache: dict[tuple[str, str], Subcategory] = dict()
#     statistic = {
#         "category": 0,
#         "subcategory": 0,
#         "quiz": 0,
#         "option": 0,
#     }
#
#     with get_session() as db:
#         try:
#             for idx, row in df.iterrows():
#                 excel_row = idx + 2
#                 category_name = _clean_str(row.get('Category'))
#                 subcategory_name = _clean_str(row.get('Subcategory'))
#                 quiz_text = _clean_str(row.get('Quiz'))
#
#                 a_text = _clean_str(row.get('A_true'))
#                 b_text = _clean_str(row.get('B'))
#                 c_text = _clean_str(row.get('C'))
#                 d_text = _clean_str(row.get('D'))
#
#                 if not (category_name and subcategory_name, quiz_text):
#                     logger.warning(
#                         "Row %s: category/subcategory/quiz bo'sh. O'tkazib yuborildi.",
#                         excel_row
#                     )
#                     continue
#
#                 options_values = [
#                     (a_text, True),
#                     (b_text, False),
#                     (c_text, False),
#                     (d_text, False)
#                 ]
#
#                 options = [(text, is_correct) for text, is_correct in options_values if text]
#
#                 if len(options) < 2:
#                     logger.warning("Row %s: Variantlar juda kam (Kamida ikkita kerak). O'tkazildi.", excel_row)
#                     continue
#
#                 # 1. Category
#                 category = category_cache.get(category_name)
#                 if not category:
#                     category = db.scalar(select(Category).where(category_name == Category.name))
#                     if category is None:
#                         category = Category(name=category_name)
#                         db.add(category)
#                         db.flush()
#                         statistic['category'] += 1
#                     category_cache[category_name] = category
#
#                 # 2. Subcategory
#                 sub_key = category_name, subcategory_name
#                 subcategory = subcategory_cache.get(sub_key)
#                 if not subcategory:
#                     subcategory = db.scalar(select(Subcategory).where(subcategory_name == Subcategory.name,
#                                                                       category.id == Subcategory.category_id))
#                     if subcategory is None:
#                         subcategory = Subcategory(name=subcategory_name, category_id=category.id)
#                         db.add(subcategory)
#                         db.flush()
#                         statistic['subcategory'] += 1
#                     subcategory_cache[sub_key] = subcategory
#
#                 # 3. Quiz
#                 quiz = db.scalar(select(Quiz).where(quiz_text == Quiz.text,
#                                                     subcategory.id == Quiz.subcategory_id))
#                 if quiz is None:
#                     quiz = Quiz(text=quiz_text, subcategory_id=subcategory.id)
#                     db.add(quiz)
#                     db.flush()
#                     statistic['quiz'] += 1
#
#                 # 4. Option
#                 for text, is_correct in options:
#                     option = db.scalar(select(Option).where(text == Option.text, quiz.id == Option.quiz_id))
#                     if option is None:
#                         option = Option(text=text, is_correct=is_correct, quiz_id=quiz.id)
#                         db.add(option)
#                         db.flush()
#                         statistic['option'] += 1
#
#             # Oxirida saqlash
#             db.commit()
#             logger.info("Excel import muvaffaqiyatli yakunlandi.")
#         except SQLAlchemyError as e:
#             db.rollback()
#             logger.exception("Excel import paytida db xatosi: %s", e)
#             raise
#         except Exception as e:
#             db.rollback()
#             logger.exception("Excel import paytida kutilmagan xatolik: %s", e)
#             raise
#
#     print(statistic)
#
#
# def test_query():
#     with get_session() as db:
#         query = select(Category)
#         categories = db.scalars(query).all()
#         print(f"Categories: {categories}")
#         for category in categories:
#             print(f"\tCat: {category}")
#             for subcategory in category.subcategories:
#                 print(f"\t\tSub: {subcategory}")
#                 for quiz in subcategory.quizzes:
#                     print(f"\t\t\tQuiz: {quiz.text}")
#                     for option in quiz.options:
#                         print(f"\t\t\t\tOption: {option.text} - ({option.is_correct})")
#
#
# if __name__ == '__main__':
#     test_query()


# Excel to DB (SQLAlchemy)

# [1] Excel Read
# [2] Session created
# [3] GET vales from cols
# [3] IF NOT EXISTS SAVE

