import tornado.ioloop
import tornado.web
import telebot

from threading import Thread

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"
bot = telebot.TeleBot(token=token)

user = -1

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    print("Got message")
    global user
    user = message.chat.id
    bot.send_message(user, "Вы подписались")


class MainHandler(tornado.web.RequestHandler):
    def get(self):

        token = self.get_argument("token")
        type = self.get_argument("type")
        comment = self.get_argument("comment")
        amount = self.get_argument("amount")

        self.write("Отправляю уведомление токену {0}, тип - {1},"
                   "количество - {2}, коммент - {3}".format(token,type,comment,amount))
        print(user)
        if user != -1:
            bot.send_message(user, "Уведомление")

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
