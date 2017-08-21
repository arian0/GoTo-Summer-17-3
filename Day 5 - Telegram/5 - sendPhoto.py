import random

import telebot

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"

bot = telebot.TeleBot(token=token)

data = {}

@bot.message_handler(commands=['photo'])
def start(message):
    user = message.chat.id
    n = random.randint(1,9)
    filename = "memes/{0}.jpg".format(n)
    image = open(filename, 'rb').read()
    bot.send_photo(user, image)


bot.polling(none_stop=True)