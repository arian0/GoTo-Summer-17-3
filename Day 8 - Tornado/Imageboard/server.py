import tornado.ioloop
import tornado.web
import json

'''
1. главная страница - список тредов - MainHandler - GET - /
2. добавление треда - MainHandler - POST - /
3. список постов в треде - ThreadHandler - GET - /thread/?id=THREAD_ID
4. добавление поста в тред - ThreadHandler - POST - /thread/?id=THREAD_ID

[
    {"name": "мемы", "posts": [
            {"author": "Аноним", "text": "текст поста"}
        ]
    },
    {"name": "мемы", "posts": [
            {"author": "Аноним", "text": "текст поста"}
        ]
    }
]
'''

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # выдача страницы с тредами
        threads = []
        with open('data.json') as file:
            threads = json.loads(file.read())

        self.render("threads.html", threads=threads)

    def post(self):
        # добавление поста
        name = self.get_argument("name")
        thread = {"name": name, "posts": []}

        threads = []
        with open('data.json') as file:
            threads = json.loads(file.read())
        threads.append(thread)

        with open('data.json', 'w') as file:
            file.write(json.dumps(threads))

        self.redirect('/')



class ThreadHandler(tornado.web.RequestHandler):
    def get(self):
        # выдача страницы с постами
        pass

    def post(self):
        # добавление поста
        pass


routes = [
    (r"/", MainHandler),
    (r"/thread/", ThreadHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()