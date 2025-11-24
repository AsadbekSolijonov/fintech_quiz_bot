from typing import List

from bot.utils.callbacks.call_data import SubcategoryData, Action
from db.models import Subcategory
from aiogram.utils.keyboard import InlineKeyboardBuilder


def builder_subcategory(subcategories: List[Subcategory]):
    builder = InlineKeyboardBuilder()
    cat_id = subcategories[0].category_id
    for sub in subcategories:
        builder.button(text=sub.name,
                       callback_data=SubcategoryData(id=sub.id, action=Action.view, cat_id=sub.category_id))
    builder.button(text="Ortga", callback_data=SubcategoryData(id=0, cat_id=cat_id, action=Action.back))
    builder.adjust(2)
    return builder.as_markup()
