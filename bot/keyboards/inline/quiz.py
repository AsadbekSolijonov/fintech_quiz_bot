from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def builder_quizzes_state():
    btn = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='Testni boshlash', callback_data='test_start'),
            InlineKeyboardButton(text='Ortga', callback_data='back_subcategory'),
        ]
    ])
    return btn
