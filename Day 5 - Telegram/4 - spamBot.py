import telebot
import time
from threading import Thread

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"

bot = telebot.TeleBot(token=token)

users = []

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Привет!")
    bot.send_message(user, "Пиши /spam, а когда надоест - /stop")
    bot.send_message(user,  "https://www.youtube.com/watch?v=rdg4lkgsQ04")

@bot.message_handler(commands=['spam'])
def spam(message):
    user = message.chat.id
    if user not in users:
        users.append(user)
        bot.send_message(user, "Берем сироп вишневый!")

@bot.message_handler(commands=['stop'])
def stop(message):
    user = message.chat.id
    print(users)
    if user in users:
        users.remove(user)
        bot.send_message(user, "Ок, все :(")

def spam():
    while True:
        for user in users:
            bot.send_message(user, "Затем сироп вишневый!")
        time.sleep(2)
def make_polling():
    bot.polling(none_stop=True)


task1 = Thread(target=make_polling)
task2 = Thread(target=spam)

task1.start()
task2.start()