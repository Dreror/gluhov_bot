import asyncio
import re
import aiogram.types
from aiogram import Bot, Router, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.enums import ParseMode
from typing import Any
from contextlib import suppress
from aiogram.exceptions import TelegramBadRequest


router = Router()
router.message.filter(F.chat.type == "supergroup")
bot = Bot("7189683921:AAFik6MriJ-mIl5Ay2yM1P_C5hP94MkAcgo")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Бот работает")


@dp.message(F.text == "Тот самый")
async def on_tot(message: Message):
    chat_id = message.chat.id
    message_for_delete = await bot.send_message(chat_id=chat_id, text="Никита гей")
    await asyncio.sleep(10)
    await bot.delete_message(chat_id=chat_id, message_id=message_for_delete.message_id)


count_warn = 0


@dp.message(F.text.count("https") & F.text.count("http") & F.text.count("t.me") & F.text.count("www"))
async def delete_spam(message: Message):
    global count_warn
    message_id = message.message_id
    chat_id = message.chat.id
    if message.from_user.id != 560303324:
        if count_warn != 1:
            message_for_delete = await bot.send_message(
                chat_id=chat_id,
                text=f"☝🏻@{message.from_user.username}, у чаті заборонено публікувати будь-які посилання, оскільки вони можуть нести рекламний характер шахраїв"
            )
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
            count_warn = count_warn + 1
            await asyncio.sleep(10)
            await bot.delete_message(chat_id=message_for_delete.chat.id, message_id=message_for_delete.message_id)
        else:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
            await delete_count()


async def delete_count():
    global count_warn
    await asyncio.sleep(20)
    count_warn = 0


async def main() -> None:
    await bot.delete_webhook(True)
    await dp.start_polling(bot)


asyncio.run(main())
