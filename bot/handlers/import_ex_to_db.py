import datetime
import os.path

from aiogram import Router, F
from aiogram.types import Message

from bot.config import BASE_DIR
from bot.services.importer import import_excel_to_database

import_router = Router()


@import_router.message(F.document)
async def import_excel(message: Message):
    file_id = message.document.file_id
    file_name = datetime.datetime.now()
    tg_file = await message.bot.get_file(file_id)
    file_path = os.path.join(BASE_DIR, f'bot/xlsx/data/{file_name}.xlsx')

    await message.bot.download_file(tg_file.file_path, file_path)
    await message.answer("Fayl yuklandi.")
    try:
        import_excel_to_database(file_path)
        await message.answer("Savollar db ga muvoffaqiyatli saqlandi.")
        # delete file
        os.remove(file_path)
    except Exception as e:
        await message.answer(f"{e}")
