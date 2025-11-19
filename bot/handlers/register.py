import re

from aiogram import html, Router
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext

from bot.states.register import Register
from db import get_session
from db.models import User

reg_router = Router()


@reg_router.message(Register.fullname)
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


@reg_router.message(Register.phone)
async def phone_state(message: Message, state: FSMContext):
    await state.update_data(phone=message.contact.phone_number)
    await message.answer('Iltimos, email‘ingizni yozing', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Register.email)


@reg_router.message(Register.email)
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
