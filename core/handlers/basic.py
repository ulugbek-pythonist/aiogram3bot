from aiogram import Bot
from aiogram.types import Message

from googletrans import Translator

translate = Translator()


async def get_start(message:Message,bot:Bot):
    await message.reply(f"Assalomu alaykum, {message.from_user.first_name}🙂\n\n🟢Tarjimon botga, xush kelibsiz!\n\n🟢O'zbekcha matn yuboring\n\n🔴Ruschasini bilib oling\n\n💪Rus tilini o'rganing")


async def tarjima(message:Message,bot:Bot):
    await message.reply(f"RU: <b>{translate.translate(message.text,dest='ru').text}</b>")