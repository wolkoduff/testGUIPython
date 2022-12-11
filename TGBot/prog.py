import telebot
import config
import os
import random

# Инициализировали бота
bot = telebot.TeleBot(config.TOKEN)


# Обработка команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Бодро пожаловать, *{0.last_name}* _{1.first_name}_!\nЯ - *{2.first_name}*, бот."
                     .format(message.from_user, message.from_user, bot.get_me()), parse_mode='markdown')


@bot.message_handler(commands=['sticker'])
def sticker(message):
    path = "TGBot\\stickers\\senya\\" # свой путь к стикерам
    senyaListStickers = os.listdir(path) # загрузить список стикеров
    size_list = len(senyaListStickers) # получить размер списка
    selected_sticker = random.randint(0, size_list) # рандомное число стикера
    pathSt = path + senyaListStickers[selected_sticker] # получить стикер
    sticker = open(pathSt, 'rb')
    bot.send_sticker(message.chat.id, sticker)

# Если создаём эхо,т.е. что не отправь, он ответит, тогда пишем
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


# Запускаем бота
bot.polling(none_stop=True)  # не останавливаться

