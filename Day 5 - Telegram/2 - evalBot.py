import telebot

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"

bot = telebot.TeleBot(token=token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    user = message.chat.id
    text = message.text
    try:
        result = eval(text)
    except Exception as e:
        result = "error"

    bot.send_message(user, str(result))

bot.polling(none_stop=True)