from aiogram.fsm.state import StatesGroup, State


class Register(StatesGroup):
    fullname = State()
    phone = State()
    email = State()
