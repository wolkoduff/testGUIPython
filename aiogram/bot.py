import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from TGBot.config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Ку! Из aiogram'а")


@dp.message_handler(commands=['first'])
async def cmd_first(message: types.Message):
    await message.reply("ФёрстЪ")


@dp.message_handler(commands=['second'])
async def cmd_sec(message: types.Message):
    await message.answer("*СекундЬ*", parse_mode='markdown')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


async def main():
    await dp.start_polling(bot)


asyncio.run(main())
