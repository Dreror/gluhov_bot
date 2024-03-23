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
bot = Bot("6018117667:AAF3wYw6mzwc6bNv5mq4dl5ZwQzmXQtAQOY")
dp = Dispatcher()


@dp.message(F.content_type.in_(aiogram.types.ContentType.NEW_CHAT_MEMBERS))
async def new_chat_members(message: Message):
    message_id = message.message_id
    chat_id = message.chat.id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)


@dp.message(F.content_type.in_(aiogram.types.ContentType.LEFT_CHAT_MEMBER))
async def exit_chat_members(message: Message):
    message_id = message.message_id
    chat_id = message.chat.id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)


count_warn = 0


@dp.message(F.text.count("https") & F.text.count("http") & F.text.count("t.me"))
async def delete_spam(message: Message):
    global count_warn
    message_id = message.message_id
    chat_id = message.chat.id
    if message.from_user.id != 560303324:
        if count_warn != 1:
            await message.answer(f"☝🏻@{message.from_user.username}, у чаті заборонено публікувати будь-які посилання, оскільки вони можуть нести рекламний характер шахраїв")
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
            count_warn = count_warn + 1
        else:
            await bot.delete_message(chat_id=chat_id, message_id=message_id)
            await delete_count()


async def delete_count():
    global count_warn
    await asyncio.sleep(1800)
    count_warn = 0


async def main() -> None:
    await bot.delete_webhook(True)
    await dp.start_polling(bot)


asyncio.run(main())
