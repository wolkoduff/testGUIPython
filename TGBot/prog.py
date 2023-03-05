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
    print(chat_id)
    # Клавиатура
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in REPLY_LIST:
        markup.add(KeyboardButton(text))

    await bot.reply_to(message, "Бодро пожаловать, *{0.last_name}* _{1.first_name}_!\nЯ - *{2.first_name}*, бот."
                     .format(message.from_user, message.from_user, bot.get_me()), parse_mode='markdown')
    await bot.reply_to(message, "Хочешь подробности?", reply_to_message_id=message.message_id, reply_markup=markup)


#    bot.send_message(chat_id, QUESTION.format(WORDS[0]))


@bot.message_handler(commands=['sticker'])
async def sticker(message):
    pathDirs = "TGBot\\stickers\\senya\\"  # свой путь к стикерам
    senyaListStickers = os.listdir(pathDirs)  # загрузить список стикеров
    size_list = len(senyaListStickers)  # получить размер списка
    selected_sticker = random.randint(0, size_list - 1)  # рандомное число стикера
    pathSt = pathDirs + senyaListStickers[selected_sticker]  # получить стикер
    #receiver_rnd = CHAT_IDS[random.randint(0, 3)]
    with open(pathSt, 'rb') as sticker:
        print(message.chat.id)
        await bot.send_sticker(message.chat.id, sticker)
    # with open(pathSt, 'rb') as sticker:
    #     print(receiver_rnd)
    #     bot.send_sticker(receiver_rnd, sticker)



@bot.message_handler(commands=['🎲dice'])
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
#bot.infinity_polling()  # не останавливаться
asyncio.run(bot.polling())

# 1356924981 - Саша
# 470054664 - Игнат
# 1623096517 - Ира
# 5834419012 - ТАнько