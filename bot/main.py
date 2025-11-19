import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from bot.config import settings as stt

# Bot token can be obtained via https://t.me/BotFather
TOKEN = stt.BOT_TOKEN
dp = Dispatcher()


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    from bot.handlers import start_router, reg_router, follow_router, import_router
    dp.include_routers(start_router, reg_router, follow_router, import_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
