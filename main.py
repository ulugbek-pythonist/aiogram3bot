import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart,Command

import asyncio
import dotenv
import logging

from core.handlers.basic import get_start, tarjima

dotenv.load_dotenv()

TOKEN = os.environ.get("TOKEN")

async def start_bot(bot:Bot):
    await bot.send_message(6763192132,text="Bot ishlashni boshladi")


async def stop_bot(bot:Bot):
    await bot.send_message(6763192132,text="Bot to'xtadi")


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - "
                        "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot  = Bot(token=str(TOKEN),parse_mode="HTML")

    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    dp.message.register(get_start,Command(commands=['start','run']))
    dp.message.register(tarjima)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())