from aiogram import html, Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from bot.keyboards.defualt.menu import builder_menu
from bot.states.register import Register
from db.models import User

from db import get_session

start_router = Router()


@start_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    txt = f"Assalomu alaykum, {html.bold(message.from_user.full_name)}!"
    await message.answer(txt)
    with get_session() as db:
        user = db.execute(select(User).where(message.chat.id == User.chat_id)).first()
    if not user:
        await message.answer("Iltimos, Ro'yxatdan o'tish uchun to'liq ism sharfingizni kiriting.")
        await state.set_state(Register.fullname)
    else:
        await message.answer('Menu ni tanglang', reply_markup=builder_menu())
