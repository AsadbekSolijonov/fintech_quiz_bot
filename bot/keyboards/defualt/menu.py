from aiogram.utils.keyboard import ReplyKeyboardBuilder


def builder_menu():
    buttons = ['Test', 'Reyting', 'Apelyatsiya', 'Feedback', 'Sozlamalar']
    btns = ReplyKeyboardBuilder()
    for button in buttons:
        btns.button(text=button)
    btns.adjust(2)
    return btns.as_markup()
