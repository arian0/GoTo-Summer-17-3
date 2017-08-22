import tornado.ioloop
import tornado.web
import telebot

from threading import Thread

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"
bot = telebot.TeleBot(token=token)

user = -1

# telegram

@bot.message_handler(commands=["auth"])
def auth_handler(message):
    message = bot.send_message(message.chat.id, "Введите токен:")
    bot.register_next_step_handler(message, make_auth)

@bot.message_handler(commands=["subscribe"])
def repeat_all_messages(message):
    print("Got message")
    global user
    user = message.chat.id
    bot.send_message(user, "Вы подписались")



def make_auth(message):
    text = message.text
    bot.send_message(message.chat.id, "Ваш токен: "+text)

#server

class MainHandler(tornado.web.RequestHandler):
    def get(self):

        token = self.get_argument("token")
        type = self.get_argument("type")
        comment = self.get_argument("comment")
        amount = self.get_argument("amount")

        print(user)
        if user != -1:
            bot.send_message(user, "Уведомление")
            self.write('{"result": "OK"}')
        else:
            self.write('{"result": "NOT FOUND"}')


def start_server():
    routes = [
            (r"/notify", MainHandler),
    ]

    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
def polling():
    bot.polling(none_stop=True)

server = Thread(target=start_server)
telegram = Thread(target=polling)

server.start()
telegram.start()
