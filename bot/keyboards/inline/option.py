from typing import List

from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.utils.callbacks.call_data import QuizData, Action, UserAnswerData
from db.models import Option


def builder_quiz_options(options: List[Option]):
    builder = InlineKeyboardBuilder()
    for option in options:
        builder.button(text=option.text,
                       callback_data=UserAnswerData(quiz_id=option.quiz_id, option_id=option.id))
    builder.adjust(2)
    return builder.as_markup()
