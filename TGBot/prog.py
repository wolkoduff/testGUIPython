import asyncio
import os.path
import random

import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot.types import *

from config import *


# TODO: сделать викторину на боте телеграм к следующему уроку


def check_answers(answer, rule_answer):
    if answer == rule_answer:
        for quest in WORDS:
            yield QUESTION.format(quest)
    else:
        return WORDS[random.randint(0, len(WORDS) - 1)]


def get_inline_keyboard(flag):
    inline_markup = InlineKeyboardMarkup()
    if flag:
        for key in INLINE_LIST:
            inline_markup.add(InlineKeyboardButton(key, callback_data=INLINE_LIST[key]))
    else:
        for key in RULE_ANSWERS:
            inline_markup.add(InlineKeyboardButton(key, callback_data=RULE_ANSWERS[key]))
    return inline_markup


# Инициализировали бота
bot = AsyncTeleBot(TOKEN)
logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)

answer = 0
text_question = ""

'''
Обработка ответа на инлайн вопрос.
1. Вопрос в инлайновом сообщении. Текст хранится в функции
2. Записать полученное сообщение в глобальную переменную
3. Получив ответ от пользователя сообщением, обработать сообщение
4. Реализовать!!!
'''

# Обработка команды /start
@bot.message_handler(commands=['start'])
async def start(message):
    chat_id = message.chat.id
    from_user = message.from_user
    last_name = from_user.last_name
    first_name = from_user.first_name
    bot_info = await bot.get_me()
    # Клавиатура
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in REPLY_LIST:
        markup.row(KeyboardButton(text))
    await bot.send_message(chat_id, "Бодро пожаловать, *{0}* _{1}_!\nЯ - *{2}*, бот."
                           .format(last_name, first_name, bot_info.first_name), parse_mode='markdown')
    await bot.reply_to(message, "Хочешь подробности?", reply_markup=markup)


#    bot.send_message(chat_id, QUESTION.format(WORDS[0]))


@bot.message_handler(commands=['sticker'])
async def sticker(message):
    path_dirs = Path("stickers")  # свой путь к стикерам
    sticker_pack_list = os.listdir(path_dirs)  # загрузить список пакетов стикеров
    selected_sticker = sticker_pack_list[random.randint(0, len(sticker_pack_list) - 1)]
    abs_path_to_stickers = Path(selected_sticker).resolve()
    stickers_list = os.listdir(abs_path_to_stickers)
    size_list = len(stickers_list)  # получить размер списка
    selected_sticker = random.randint(0, size_list - 1)  # рандомное число стикера
    path_sticker = stickers_list[selected_sticker]  # получить стикер
    # receiver_rnd = CHAT_IDS[random.randint(0, 3)]
    chat_id = message.chat.id
    with open(path_sticker, 'rb') as sticker:
        await bot.send_sticker(chat_id, sticker)
    # with open(path_sticker, 'rb') as sticker:
    #     print(receiver_rnd)
    #     bot.send_sticker(receiver_rnd, sticker)


async def dice(message):
    chat_id = message.chat.id
    await bot.send_dice(chat_id, emoji="🎲")


async def bowling(message):
    chat_id = message.chat.id
    await bot.send_dice(chat_id, emoji="🎳")


async def casino(message: Message):
    chat_id = message.chat.id
    await bot.send_dice(chat_id, emoji="🎰")

async def darts(message):
    chat_id = message.chat.id
    await bot.send_dice(chat_id, emoji="🎯")

async def basketball(message):
    chat_id = message.chat.id
    await bot.send_dice(chat_id, emoji="🏀")

async def football(message):
    chat_id = message.chat.id
    await bot.send_dice(chat_id, emoji="⚽")


@bot.message_handler(commands=['poll'])
async def send_pool(message: telebot.types.Message):
    chat_id = message.chat.id
    answer_list = ["На пики сам сяду, стул другу подставлю (потому что без друзей)", "Питон ломается, джава "
                                                                                     "выкидывается"]
    await bot.send_poll(chat_id=chat_id, question="Есть два стула. На одном python-говёный, на другом "
                                                  "java-просвящённый. На какой стул"
                                                  " сам сядешь, а какой другу подставишь?",
                        options=answer_list, is_anonymous=True, allows_multiple_answers=True,
                        reply_markup=get_inline_keyboard(True))

# Если создаём эхо,т.е. что не отправь, он ответит, тогда пишем
@bot.message_handler(content_types=['text'])
async def echo(message):
    chat_id = message.chat.id
    text = message.text
    if text.isnumeric():
        try:
            res_string = text_question.split(" ")
            one = 0
            two = 0
            for x in res_string:
                if x.isnumeric():
                    if one == 0:
                        one = int(x)
                    else:
                        two = int(x)
            res = one + two
            if int(text) == res:
                await bot.reply_to(message, "Правильно!")
            else:
                await bot.reply_to(message, "Неправильно бл..ть!")
        except Exception as e:
            await bot.send_message(chat_id, str(e))

    if text in REPLY_LIST:
        if text == "🎲dice":
            await dice(message)
        elif text == "🎳bowling":
            await bowling(message)
        elif text == "🎰casino":
            await casino(message)
        elif text == "🎯darts":
            await darts(message)
        elif text == "⚽football":
            await football(message)
        elif text == "🏀basketball":
            await basketball(message)
    # receiver_rnd = CHAT_IDS[random.randint(0, len(CHAT_IDS))]
    # bot.forward_message(disable_notification=True, chat_id= )

    # inline_keyboard =

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
    # await bot.send_message(chat_id, "БУУУУУУМ", reply_to_message_id=message.message_id)

@bot.message_handler(content_types=['sticker'])
async def echo_sticker(message):
    file_uid = message.sticker.file_unique_id
    with open("stickers_list_receive.txt", "r+") as file:
        memory_stickers_list = file.readlines()

    if len(memory_stickers_list) == 0:
        with open("stickers_list_receive.txt", 'a+') as file:
            file.write(file_uid + "\n")
        await bot.reply_to(message, 'Я записал новый')
    else:
        with open("stickers_list_receive.txt", "r+") as file:
            file_id = file.readline().replace("\n", "")
            if file_id == file_uid:
                await bot.reply_to(message, 'Мазафака, у меня он уже есть!')
            else:
                memory_stickers_list.append(file_uid + "\n")
                await bot.reply_to(message, 'Я записал этот стикер себе в память')

        with open("stickers_list_receive.txt", "a+") as file:
            for file_id in memory_stickers_list:
                file_in_list = file.next().replace("\n", "")
                if file.readline().replace("\n", "") != file_id.replace("\n", ""):
                    file.write(file_id)

@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call):
    global text_question
    if call.data == "excellent":
        await bot.answer_callback_query(call.id, "УРааааа!", show_alert=True)
    elif call.data == "fuck":
        one = random.randint(1, 9)
        two = random.randint(1, 9)
        text_question = "Сколько будет {0} + {1}".format(one, two)
        await bot.answer_callback_query(call.id, text_question, show_alert=True)
        await bot.edit_message_reply_markup(call.message.chat.id, call.message.id, reply_markup=get_inline_keyboard(False))

# Запускаем бота
# bot.infinity_polling()  # не останавливаться
asyncio.run(bot.polling())

# TODO: обработка сообщений в супер-группе

# 1356924981 - Саша
# 470054664 - Игнат
# 1623096517 - Ира
# 5834419012 - ТАнько
