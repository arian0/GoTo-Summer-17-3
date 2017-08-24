import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h2>Hello, world</h2>")
        self.write("<img width='400px' src='https://icdn.lenta.ru/images/2016/08/04/12/20160804125254027/pic_d86815bab0fb639499d43ca75ed4760f.jpg'>")
        self.write("<form action='/hello'><label>Как вас зовут?</label><input name='name' /><button>Отправить</button></form>")

# localhost:8888/hello?name=Rostislav
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "аноним")
        self.render("hello_template.html", name=name)


routes = [
    (r"/", MainHandler),
    (r"/hello", HelloHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()