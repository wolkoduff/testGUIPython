import asyncio
import random

import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.types import *

# TODO: свой файл конфига сюда импортируете

bot = AsyncTeleBot('СЮДА СВОЙ ТОКЕН БОТА')
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

@bot.message_handler(commands=['start'])
async def start(message):
    chat_id = message.chat.id
    from_user = message.from_user
    last_name = from_user.last_name
    first_name = from_user.first_name
    bot_info = await bot.get_me()
    await bot.send_message(chat_id, "Здравствуйте, *{0}* _{1}_!\nЯ - *{2}*, бот." # *жирный*, _курсив_
                           .format(last_name, first_name, bot_info.first_name), parse_mode='markdown', reply_markup=None) #TODO: сделать клавиатуру согласно задания
    #TODO: Кнопка рандом - кидает рандомный дайс
    #      Кнопка стикер - кидает рандомный стикер из пакета стикеров, что скачивали ранее либо используем имеющийся
    #      Кнопка картинка - рандомную картинку с подписью


# Запускаем бота работать
asyncio.run(bot.polling())
