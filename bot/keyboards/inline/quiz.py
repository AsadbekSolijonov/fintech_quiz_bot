from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.utils.callbacks.call_data import QuizData, Action


def builder_quizzes_state(cat_id):
    builder = InlineKeyboardBuilder()
    builder.button(text="Testni boshlash", callback_data=QuizData(id=0, sub_id=0, cat_id=cat_id, action=Action.start))
    builder.button(text="Ortga", callback_data=QuizData(id=0, sub_id=0, cat_id=cat_id, action=Action.back))
    builder.adjust(1)
    return builder.as_markup()
