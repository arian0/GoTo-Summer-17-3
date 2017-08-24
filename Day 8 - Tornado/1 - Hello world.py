import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("<h2>Hello, world</h2>")
        self.write("<img width='400px' src='https://icdn.lenta.ru/images/2016/08/04/12/20160804125254027/pic_d86815bab0fb639499d43ca75ed4760f.jpg'>")

# localhost:8888/hello?name=Rostislav
class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument("name", "аноним")
        self.write("Привет, {0}!".format(name))

routes = [
    (r"/", MainHandler),
    (r"/hello", HelloHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()