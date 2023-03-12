import os.path
from pathlib import Path

from telebot.async_telebot import AsyncTeleBot
import asyncio
from config import *
import random
from telebot.types import *


# TODO: сделать викторину на боте телеграм к следующему уроку


def check_answers(answer, rule_answer):
    if answer == rule_answer:
        for quest in WORDS:
            yield QUESTION.format(quest)
    else:
        return WORDS[random.randint(0, len(WORDS) - 1)]


# Инициализировали бота
bot = AsyncTeleBot(TOKEN)

answer = 0


# Обработка команды /start
@bot.message_handler(commands=['start'])
async def start(message):
    chat_id = message.chat.id
    last_name = message.from_user.last_name
    first_name = message.from_user.first_name
    print(chat_id)
    # Клавиатура
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in REPLY_LIST:
        markup.add(KeyboardButton(text))

    await bot.send_message(chat_id, "Бодро пожаловать, *{0}* _{1}_!\nЯ - *{2}*, бот."
                           .format(last_name, first_name, bot.get_me().first_name), parse_mode='markdown')
    await bot.reply_to(message, "Хочешь подробности?", reply_markup=markup)


#    bot.send_message(chat_id, QUESTION.format(WORDS[0]))


@bot.message_handler(commands=['sticker'])
async def sticker(message):
    pathDirs = Path("stickers")  # свой путь к стикерам
    listStickerPacks = os.listdir(pathDirs)  # загрузить список пакетов стикеров
    selectedSticker = listStickerPacks[random.randint(0, len(listStickerPacks) - 1)]
    absPathToStickers = Path(pathDirs + "\\" + selectedSticker).resolve()
    listStickers = os.listdir(absPathToStickers)
    size_list = len(listStickers)  # получить размер списка
    selected_sticker = random.randint(0, size_list - 1)  # рандомное число стикера
    pathSt = listStickers[selected_sticker]  # получить стикер
    # receiver_rnd = CHAT_IDS[random.randint(0, 3)]
    chatId = message.chat.id
    with open(pathSt, 'rb') as sticker:
        print(message.chat.id)
        await bot.send_sticker(chatId, sticker)
    # with open(pathSt, 'rb') as sticker:
    #     print(receiver_rnd)
    #     bot.send_sticker(receiver_rnd, sticker)


@bot.message_handler(content_types=["🎲dice"])
async def dice(message):
    chat_id = message.chat.id
    print(chat_id)
    await bot.send_dice(chat_id, emoji="🎲")


@bot.message_handler(commands=['🎳bowling'])
async def bowling(message):
    chat_id = message.chat.id
    print(chat_id)
    await bot.send_dice(chat_id, emoji="🎳")


@bot.message_handler(commands=['🎰casino'])
async def casino(message):
    chat_id = message.chat.id
    print(chat_id)
    await bot.send_dice(chat_id, emoji="🎰")


# Если создаём эхо,т.е. что не отправь, он ответит, тогда пишем
@bot.message_handler(content_types=['text'])
async def echo(message):
    # bot.send_message(message.chat.id, message.text)
    chat_id = message.chat.id
    # text = message.text.lower()
    # print(text)
    # if message.chat.type == 'private':
    #     if text == REPLY_LIST[0]:
    #         bot.send_message(chat_id, "LOOOOOOOL, ЗАТРАЛЛЕН🤣")
    #     elif text == REPLY_LIST[1]:
    #         bot.send_message(chat_id, "Больно и хотелось...")
    #     elif text == REPLY_LIST[2]:
    #         bot.send_message(chat_id, "ЧИВОООООО?")
    #     elif text == REPLY_LIST[3]:
    #         bot.send_message(chat_id, "Реклама СБП?")
    #     else:
    #         bot.send_message(chat_id, "ДУПЛО СЕБЕ ОТМЕНИ!")
    # bot.send_message(chat_id, QUESTION.format(WORDS[0]))
    await bot.send_message(chat_id, "БУУУУУУМ", reply_to_message_id=message.message_id)

# Запускаем бота
# bot.infinity_polling()  # не останавливаться
asyncio.run(bot.polling())

# 1356924981 - Саша
# 470054664 - Игнат
# 1623096517 - Ира
# 5834419012 - ТАнько
