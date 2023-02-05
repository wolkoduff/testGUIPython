import telebot
from config import *
import random

# TODO: сделать викторину на боте телеграм к следующему уроку

from telebot.types import *

def check_answers(answer, rule_answer):
    if answer == rule_answer:
        for quest in WORDS:
            yield QUESTION.format(quest)
    else:
        return WORDS[random.randint(0, len(WORDS) - 1)]

# Инициализировали бота
bot = telebot.TeleBot(TOKEN)

answer = 0

# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    # Клавиатура
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for text in REPLY_LIST:
        markup.add(KeyboardButton(text))

    chat_id = message.chat.id

    '''
    bot.send_message(chat_id, "Бодро пожаловать, *{0.last_name}* _{1.first_name}_!\nЯ - *{2.first_name}*, бот."
                     .format(message.from_user, message.from_user, bot.get_me()), parse_mode='markdown')
    bot.send_message(chat_id, "Хочешь подробности?", reply_markup=markup)
    '''
    bot.send_message(chat_id, QUESTION.format(WORDS[0]))

@bot.message_handler(commands=['sticker'])
def sticker(message):
    path = "TGBot\\stickers\\senya\\"  # свой путь к стикерам
    senyaListStickers = os.listdir(path)  # загрузить список стикеров
    size_list = len(senyaListStickers)  # получить размер списка
    selected_sticker = random.randint(0, size_list - 1)  # рандомное число стикера
    pathSt = path + senyaListStickers[selected_sticker]  # получить стикер
    stiker = open(pathSt, 'rb')
    bot.send_sticker(message.chat.id, stiker)


# Если создаём эхо,т.е. что не отправь, он ответит, тогда пишем
@bot.message_handler(content_types=['text'])
def echo(message):
    # bot.send_message(message.chat.id, message.text)
    chat_id = message.chat.id
    text = message.text
    if message.chat.type == 'private':
        if text == REPLY_LIST[0]:
            bot.send_message(chat_id, "LOOOOOOOL, ЗАТРАЛЛЕН🤣")
        elif text == REPLY_LIST[1]:
            bot.send_message(chat_id, "Больно и хотелось...")
        elif text == REPLY_LIST[2]:
            bot.send_message(chat_id, "ЧИВОООООО?")
        elif text == REPLY_LIST[3]:
            bot.send_message(chat_id, "Реклама СБП?")
        else:
            bot.send_message(chat_id, "ДУПЛО СЕБЕ ОТМЕНИ!")
    bot.send_message(chat_id, QUESTION.format(WORDS[0]))

# Запускаем бота
bot.polling(none_stop=True)  # не останавливаться
