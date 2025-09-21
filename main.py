import telebot
from telebot import types
import random

user_games = {}
anekdots = [
    "— Доктор, я везде слышу голоса... \n— А вы пробовали выключить телевизор?",
    "Студент приходит на экзамен, профессор говорит: \n— У вас два пути: либо вы сдаёте экзамен, либо я вас заваливаю. \nСтудент отвечает: \n— Профессор, давайте пойдём по третьему пути — мирно разойдёмся!",
    "Учительница спрашивает Вовочку: \n— Почему ты вчера не был в школе? \n— Я поехал с папой на рыбалку. \n— А кто тебе разрешил? \n— Доктор. Он сказал, что свежий воздух полезен!",
    "Муж говорит жене: \n— Дорогая, я похудел! \nЖена: \n— Ты просто выдохнул..."
]

TOKEN = "#"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🎲 бросить кубик")
    btn2 = types.KeyboardButton("😊 поздороваться")
    btn3 = types.KeyboardButton("❓ показать помощь")
    btn4 = types.KeyboardButton("Угадай число!")
    btn5 = types.KeyboardButton("Я хочу анекдот😶‍🌫️!")
    markup.add(btn1, btn2, btn3, btn4, btn5)

    
    bot.send_message(message.chat.id, "Hello I am your first bot. \n Choose what to do", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def reply(message):
    if message.text == "🎲 бросить кубик":
        num = random.randint(1, 6)
        bot.send_message(message.chat.id, f"Ты выбросил: 🎲 {num}")
    elif message.text == "😊 поздороваться":
        bot.send_message(message.chat.id, " Привет рад тебя видеть! ")
    elif message.text == "❓ показать помощь":
        bot.send_message(message.chat.id, " Я могу выбросить кубик \n я могу поздороваться \n показать все команды")
    elif message.text == "Угадай число!":
        user_games[message.chat.id] = random.randint(1,5)
        bot.send_message(message.chat.id, "Я загадал число от 1 до 5 Попробуй угадать")
    elif message.text == "Я хочу анекдот😶‍🌫️!":
        bot.send_message(message.chat.id, random.choice(anekdots))

        
    elif message.chat.id in user_games:
        try:
            guess = int(message.text)
            if guess == user_games[message.chat.id]:
                bot.send_message(message.chat.id, "Congrats u got it")
                del user_games[message.chat.id]
            else:
                bot.send_message(message.chat.id, "Ne ugadal try again")
        except ValueError:
            bot.send_message(message.chat.id, "NAPIWI ot 1 do 5!!!")
            
    else:
        bot.send_message(message.chat.id, " I dont understand u")


bot.polling(none_stop = True)
