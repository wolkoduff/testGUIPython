# Первым делом, мы устанавливаем API-лку телеграмм бота по комментарию ниже
# pip install pytelegrambotapi

""" Итак, программа написания собственного телеграм-бота с локальным размещением и запуском в рамках занятий по программе
    "Программирование на Python (2 год)

    Рассчитано на 4 занятия:
    04.12.22 - создаём своего собственного бота в телеграмм, изучение, что будет рассмотрено и подготовлено
    11.12.22 - первые игрушки с ботом: обработка комманд, обработка специальных комманд "/start", "/help", "/settings" и
               "/stop", "проба пера"
    18.12.22 - Кнопки для отображения в телеге, переход по гипер-ссылкам
    25.12.22 - Самостоятельная работа по созданию бота 1 час, 30 минут на проверку работы бота в телеграмме
               Заготовки на новый год, что будем проходить и делать, а также, что хотелось бы изучить
"""


# Создать файл конфигурации для его импорта.
# ВАЖНО: правила хорошего тона предусматривают создание файлов конфигурации и настроек, а не тащить всё в одном файле
# В файле config.py пишем TOKEN = 'токен', куда вместо слова @токен вставляем полученный токен от @BotFather

class config:
    TOKEN = ''  # token from @BotFather


import telebot

bot = telebot.TeleBot(config.TOKEN)


# Если создаём эхо,т.е. что не отправь, он ответит, тогда пишем
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать, _{0.first_name}_!\nЯ - *{1.first_name}*, бот ".format(
        message.from_user, bot.get_me()), parse_mode='markdown'#, reply_markup=keyboard
                     )


@bot.message_handler(commands=['Стикер'])
def send_sticker(message):
    stiker = open('stikers/...', 'rb')
    bot.send_sticker(message.chat.id, stiker)

    # keyboard
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = telebot.types.KeyboardButton("Первая кнопка")
    item2 = telebot.types.KeyboardButton("Вторая кнопка")
    markup.add(item1, item2)


# Запускаем бота
bot.polling(none_stop=True)  # не останавливаться
