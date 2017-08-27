import tornado.ioloop
import tornado.web
import json
from bson import ObjectId

from pymongo import MongoClient

'''
1. главная страница - список тредов - MainHandler - GET - /
2. добавление треда - MainHandler - POST - /
3. список постов в треде - ThreadHandler - GET - /thread?id=THREAD_ID
4. добавление поста в тред - ThreadHandler - POST - /thread?id=THREAD_ID

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

# создать конекшн к монге
connection = MongoClient("mongodb://user:password@ds159963.mlab.com:59963/goto_imageboard")

# выбрать бд
database = connection['goto_imageboard']

# выбрать коллекцию
threads_collection = database['threads']

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # выдача страницы с тредами
        threads = list(threads_collection.find())

        self.render("threads.html", threads=threads)

    def post(self):
        # добавление треда
        name = self.get_argument("name")
        thread = {"name": name, "posts": []}

        threads_collection.insert(thread)

        self.redirect('/')



class ThreadHandler(tornado.web.RequestHandler):
    def get(self):
        # выдача страницы с постами
        # TODO: Написать шаблон для страницы с постами (похожий на главную страницу)
        # TODO: Взять тред из монги, у которого {'_id': ObjectId(self.get_argument('id'))}
        id = self.get_argument('id')
        thread = threads_collection.find_one({'_id': ObjectId(id)})

        # TODO: Зарендерить шаблон с постами этого треда
        self.render("posts.html", thread=thread)

    def post(self):
        # добавление поста
        # TODO: Получить параметры из запроса (self.get_argument...)
        id = self.get_argument('id')
        author = self.get_argument('author')
        text = self.get_argument('text')

        # TODO: сделать новый пост
        post = {"author": author, "text": text}

        # TODO: добавить пост в тред и сохранить в монге
        thread = threads_collection.find_one({'_id': ObjectId(id)})
        thread['posts'].append(post)
        threads_collection.update({'_id': ObjectId(id)}, thread)

        # TODO: редирект на страницу с постами
        self.redirect('/thread?id={0}'.format(id))


routes = [
    (r"/", MainHandler),
    (r"/thread", ThreadHandler),
]

app = tornado.web.Application(routes, debug=True)
app.listen(8888)
tornado.ioloop.IOLoop.current().start()