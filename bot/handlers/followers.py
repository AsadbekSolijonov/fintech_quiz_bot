from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy import select, func
from db.models import User

from db import get_session

follow_router = Router()


@follow_router.message(Command('followers'))
async def followers_count(message: Message):
    with get_session() as db:
        # SQL: select count(*) from users;
        # ORM: db.scalar(select(func.count()).select_from(User))
        count = db.scalar(select(func.count()).select_from(User))
        await message.answer(f'🔔 Obunachilar soni {count} ta.')
