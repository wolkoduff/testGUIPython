import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from TGBot.config import *

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


# pip install -U --pre aiogram - обновить на aiogram 3.0, поскольку у всех 2.25
# pip uninstall aiogram

@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.reply("Ку! Из aiogram'а")


@dp.message(Command(commands=["reply"]))
async def cmd_first(message: types.Message):
    await message.reply("ФёрстЪ")


@dp.message(Command(commands=["answer"]))
async def cmd_sec(message: types.Message):
    await message.answer("*СекундЬ*", parse_mode='markdown')


@dp.message(Command(commands=["bowling"]))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎳")  # Если хотим отправить в конкретный чат, тогда необходимо получить
    # идентификатор чата
    await message.answer_dice(emoji="🎲")  # Если хотим отправить в конкретный чат, тогда необходимо получить
    # идентификатор чата
    await message.answer_dice(emoji="🎰")  # Если хотим отправить в конкретный чат, тогда необходимо получить
    # идентификатор чата
    await message.answer_dice(emoji="🎯")  # Если хотим отправить в конкретный чат, тогда необходимо получить
    # идентификатор чата
    await message.answer_dice(emoji="⚽")  # Если хотим отправить в конкретный чат, тогда необходимо получить
    # идентификатор чата
    await message.answer_dice(emoji="🏀")  # Если хотим отправить в конкретный чат, тогда необходимо получить
    # идентификатор чата


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
