import telebot

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"

bot = telebot.TeleBot(token=token)

data = {}

@bot.message_handler(commands=['start', 'help'])
def start(message):
    user = message.chat.id
    bot.send_message(user, "Привет!")
    bot.send_message(user, "Пиши /remember и я запомню, напиши /remind и я скажу, что я запомнил.")

@bot.message_handler(commands=['remember'])
def remember(message):
    global data
    text = message.text
    user = message.chat.id
    data[user] = text[10:]
    bot.send_message(user, "Я запомнил!")


@bot.message_handler(commands=['remind'])
def remind(message):
    user = message.chat.id
    if user not in data:
        bot.send_message(user, "Чувак, ты не просил ничего запомнить :(")
    else:
        m = data[user]
        bot.send_message(user, "Ты просил запомнить: {0}".format(m))

bot.polling(none_stop=True)