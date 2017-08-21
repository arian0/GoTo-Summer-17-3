import telebot

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"

bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    user = message.chat.id
    text = message.text
    bot.send_message(user, text)

bot.polling(none_stop=True)