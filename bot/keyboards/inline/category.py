from typing import List

from db.models import Category
from aiogram.utils.keyboard import InlineKeyboardBuilder


def builder_category(categories: List[Category]):
    builder = InlineKeyboardBuilder()
    for category in categories:
        builder.button(text=category.name, callback_data=f"cat:{category.id}")
    builder.adjust(2)
    return builder.as_markup()
