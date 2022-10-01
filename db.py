import telebot
from telebot import types
import sqlite3

#bot
token = "5290253471:AAHb5yWJ09ofq8nLdnY16YJZ4hWpn5GMg3Y"
bot = telebot.TeleBot(token)

num_start = 0

@bot.message_handler(commands=["start"])
def start(message):
    global num_start
    num_start += 1
    text = f'Здравствуйте! Я помощник клуба "ШАРОБОТ", помогу понять, какие занятия подойдут Вашему ребенку.\n\nКликните по кнопке ниже 👇 чтобы начать тестирование.'
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*[types.KeyboardButton(name) for name in ['💼 Начать тестирование']]) 

    with open('image.jpg', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption=text, reply_markup=keyboard, parse_mode="HTML")


    # bot.send_message(message.chat.id, 'Здравствуйте! Я помощник клуба "ШАРОБОТ", помогу понять, какие занятия подойдут Вашему ребенку.\n\nКликните по кнопке ниже 👇 чтобы начать тестирование.')


    # global num_start
    # num_start += 1
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    # keyboard.add(*[types.KeyboardButton(name) for name in ['💼 Кнопка 1', '📊 Кнопка 2', '🚀 Кнопка 3', 'Кнопка 4']])

    #connect = sqlite3.connect("sharobot.db")
    #cursor = connect.cursor()

    #cursor.execute("""CREATE TABLE IF NOT EXISTS table_name (
    #    id integer,
    #    name text
    #    )""")

    #connect.commit()

    ##add values in fields
    #usersId = [message.chat.id]
    #cursor.execute("INSERT INTO table_name values(?)", usersId)
    #connect.commit()

#pooling
bot.polling()