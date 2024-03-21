import asyncio
import re
import datetime
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
async def new_chat_members1(message: Message):
    message_id = message.message_id
    chat_id = message.chat.id
    await bot.delete_message(chat_id=chat_id, message_id=message_id)


@dp.message(F.text.startswith("https", "http", "t.me"))
async def delete_spam(message: Message):
    message_id = message.message_id
    chat_id = message.chat.id
    await message.answer("☝🏻 У чаті заборонено публікувати будь-які посилання, оскільки вони можуть нести рекламний характер шахраїв")
    await bot.delete_message(chat_id=chat_id, message_id=message_id)


async def main() -> None:
    await bot.delete_webhook(True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
