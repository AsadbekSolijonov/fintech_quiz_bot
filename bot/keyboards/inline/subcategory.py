from typing import List

from bot.utils.callbacks.call_data import SubcategoryData
from db.models import Subcategory
from aiogram.utils.keyboard import InlineKeyboardBuilder


def builder_subcategory(subcategories: List[Subcategory]):
    builder = InlineKeyboardBuilder()
    for sub in subcategories:
        builder.button(text=sub.name, callback_data=SubcategoryData(id=sub.id))
    builder.button(text="Ortga", callback_data='back_to_cat')
    builder.adjust(2)
    return builder.as_markup()
