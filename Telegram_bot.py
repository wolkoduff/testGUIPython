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
    TOKEN = '5821638217:AAGkeYEvsWlltgbarkYnLlfivJSWURYkI-c'  # token from @BotFather


import telebot

from telebot import types

bot = telebot.TeleBot(config.TOKEN)


# Если создаём эхо,т.е. что не отправь, он ответит, тогда пишем
@bot.message_handler(commands=['start', 'stop'])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать, _{0.first_name}_!\nЯ - *{1.first_name}*, бот ".format(
        message.from_user, bot.get_me()), parse_mode='markdown')


def stop(message):
    bot.stop_bot()


#@bot.message_handler(commands=['Стикер'])
#def send_sticker(message):
#    stiker = open('stikers/...', 'rb')
#    bot.send_sticker(message.chat.id, stiker)


@bot.message_handler(content_types=['text'])
def echo(message):
    # bot.send_message(message.chat.id, message.text)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Первая кнопка")
    item2 = types.KeyboardButton("Вторая кнопка")
    markup.add(item1, item2)

    inline_markup = types.InlineKeyboardMarkup(row_width=4)
    my_list = {"Хорошо": "good",
            "Не очень": "badly",
            "Петух": "chicken",
            "БК": "burger_king"}
    for i in range(4):
        key = list(my_list.keys())[i]
        value = list(my_list.values())[i]
        inline_markup.add(types.InlineKeyboardButton(key, callback_data=value))

    if message.chat.type == 'private':
        if message.text == 'Первая кнопка':
            bot.send_message(message.chat.id, "Ответ на первую кнопку", reply_markup=inline_markup)
        else:
            bot.send_message(message.chat.id, "Я не знаю, что тебе ответить", reply_markup=inline_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            
            chat_id = call.message.chat.id

            if call.data == "good":
                bot.send_message(chat_id, "Это ж хорошо, мазафака")
            elif call.data == "bad":
                bot.send_message(chat_id, "НУ долбанный крот в рот, соболезную")
            elif call.data == "chicken":
                bot.send_message(chat_id, "Сам петух! У нас Ростикс")
            elif call.data == "burger_king":
                bot.send_message(chat_id, "Вот и иди по адресу королевскому")
            else:
                bot.send_message(chat_id, "НИ ПОНЯЛ НИЧЕГО")

            # remove inline buttons
            bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="БК",
                                  reply_markup=None)

            # Уведомления
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True,
                                    text="Какое-то уведомление просто так")

    except Exception as ex:
        print(repr(ex))


# Запускаем бота
bot.polling(none_stop=True)  # не останавливаться
