import asyncio
import logging
import sys
import re
from os import getenv
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from bot.config import settings as stt
from sqlalchemy import select, func

from db import get_session
from db.models import User

# Bot token can be obtained via https://t.me/BotFather
TOKEN = stt.BOT_TOKEN
dp = Dispatcher()


# FSM
# 1 - Ism Familya
# 2 - Phone number
# 3 - Email

# State Formasi
class Register(StatesGroup):
    fullname = State()
    phone = State()
    email = State()


@dp.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext) -> None:
    txt = f"Assalomu alaykum, {html.bold(message.from_user.full_name)}!"
    await message.answer(txt)
    with get_session() as db:
        user = db.execute(select(User).where(message.chat.id == User.chat_id)).first()
    if not user:
        await message.answer("Iltimos, Ro'yxatdan o'tish uchun to'liq ism sharfingizni kiriting.")
        await state.set_state(Register.fullname)
    else:
        await message.answer('Siz avval ro‘yxatdan o‘tgansiz.')


@dp.message(Register.fullname)
async def fullname_state(message: Message, state: FSMContext):
    await state.update_data(fullname=message.text)
    ctc_btn = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text='Telefon ulashish', request_contact=True)
        ]
    ],
        resize_keyboard=True,
        input_field_placeholder='Yozmang...'
    )
    await message.answer('Iltimos telefon raqamingizni ulashing', reply_markup=ctc_btn)
    await state.set_state(Register.phone)


@dp.message(Register.phone)
async def phone_state(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await message.answer('Iltimos, email‘ingizni yozing', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Register.email)


@dp.message(Register.email)
async def phone_state(message: Message, state: FSMContext):
    ptn = r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
    if re.match(ptn, message.text):
        await state.update_data(email=message.text)

        data = await state.get_data()

        fullname = data.get('fullname')
        phone = data.get('phone')
        email = data.get('email')
        chat_id = message.chat.id

        # database save
        with get_session() as db:
            user = User(fullname=fullname,
                        chat_id=chat_id,
                        phone=phone,
                        email=email)
            db.add(user)
            db.commit()
            db.refresh(user)
            print(f"DB SAVE: {user}")

        txt = (f"🧑🏼‍ Ism: {html.bold(fullname)}\n"
               f"📲 Phone: {html.bold(phone)}\n"
               f"📧 Email: {html.bold(email)}")
        await message.answer(text=txt)
        await state.clear()

    else:
        await message.answer('Iltimos to‘g‘ri formatdagi email kiriting.')


@dp.message(Command('followers'))
async def followers_count(message: Message):
    with get_session() as db:
        # SQL: select count(*) from users;
        # ORM: db.scalar(select(func.count()).select_from(User))
        count = db.scalar(select(func.count()).select_from(User))
        await message.answer(f'🔔 Obunachilar soni {count} ta.')


@dp.message()
async def echo(message: Message):
    await message.answer(message.text)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
