from aiogram.types import Message, CallbackQuery
from aiogram import Router, F

from bot.keyboards.inline.category import builder_category
from bot.keyboards.inline.subcategory import builder_subcategory
from bot.utils.quiz.category import get_categories
from bot.utils.quiz.subcategory import get_subcategories

test_router = Router()


@test_router.message(F.text == 'Test')
async def test_handler(message: Message):
    categories = get_categories()
    if categories:
        ct_btns = builder_category(categories)
        await message.answer("Savollar kategoriyasi.", reply_markup=ct_btns)
    else:
        await message.answer("Savollar kategoriyasi mavjud emas!")


@test_router.callback_query(F.data.startswith("cat:"))
async def handler_category(call: CallbackQuery):
    _, cat_id = call.data.split(':')  # cat:16 or cat:17
    subcategories = get_subcategories(cat_id=int(cat_id))
    if subcategories:
        sb_btns = builder_subcategory(subcategories)
        await call.message.edit_text("Subkategoriyalar", reply_markup=sb_btns)
    else:
        await call.message.answer(text=f"Subcategoriyalar mavjud emas.")


@test_router.callback_query(F.data == 'back_to_cat')
async def back_category_handler(call: CallbackQuery):
    categories = get_categories()
    if categories:
        ct_btns = builder_category(categories)
        await call.message.edit_text("Savollar kategoriyasi.", reply_markup=ct_btns)
    else:
        await call.message.edit_text("Savollar kategoriyasi mavjud emas!")
