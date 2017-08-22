import tornado.ioloop
import tornado.web
import telebot
from threading import Thread


# делаем бота
token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"
bot = telebot.TeleBot(token=token)

# тут храним id пользователя
# TODO: заменить словарем id <-> token
user = -1

# telegram
# авторизация в два шага
# 1) спрашиваем токен
# 2) проверяем его правильность
@bot.message_handler(commands=["auth"])
def auth_handler(message):
    message = bot.send_message(message.chat.id, "Введите токен:")
    bot.register_next_step_handler(message, make_auth)

# TODO: сделать реальный запрос к API, если успех - положить id в словарь
def make_auth(message):
    text = message.text
    bot.send_message(message.chat.id, "Ваш токен: "+text)

# подписка на уведомления - можно будет убрать
@bot.message_handler(commands=["subscribe"])
def repeat_all_messages(message):
    print("Got message")
    global user
    user = message.chat.id
    bot.send_message(user, "Вы подписались")





#server
# серверная часть, нужна для уведомлений. Уведомления присылать будет Егор
class MainHandler(tornado.web.RequestHandler):
    def get(self):

        token = self.get_argument("token")
        type = self.get_argument("type")
        comment = self.get_argument("comment")
        amount = self.get_argument("amount")

        print(user)
        # TODO: проверить есть ли пользователь среди атворизованных и отправить нормальное уведомление с понятным текстом
        if user != -1:
            bot.send_message(user, "Уведомление")
            self.write('{"result": "OK"}')
        else:
            self.write('{"result": "NOT FOUND"}')

# запуск веб сервера
def start_server():
    routes = [
            (r"/notify", MainHandler),
    ]

    app = tornado.web.Application(routes)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
def polling():
    bot.polling(none_stop=True)

# в одном потоке телеграм, в другом сервер
server = Thread(target=start_server)
telegram = Thread(target=polling)

server.start()
telegram.start()
