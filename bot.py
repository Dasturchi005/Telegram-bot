import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
import wikipedia
from dotenv import load_dotenv

# .env fayldan tokenni yuklab olish
load_dotenv()
TOKEN = getenv("BOT_TOKEN")

wikipedia.set_lang('uz')

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}! sizga qanday yordam bera olishim mumkin? ")

@dp.message()
async def wikipedia_bot(message: Message) -> None:
    try:
        report = wikipedia.summary(message.text)
        await message.answer(report)
    except Exception:
        await message.answer("Bu maqola topilmadi. Iltimos, boshqa so'z kiriting.")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
