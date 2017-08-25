from pymongo import MongoClient

# mlab.com

# создать конекшн к монге
connection = MongoClient("mongodb://user:password@ds159963.mlab.com:59963/goto_imageboard")

# выбрать бд
database = connection['goto_imageboard']

# выбрать коллекцию
threads_collection = database['threads']

# добавление данных
threads_collection.insert({"name": "мемы", "posts": []})

threads_collection.insert([
    {"name": "мемы1", "posts": []},
    {"name": "мемы1", "posts": []}
                           ])

# получение данных

threads = list(threads_collection.find())
for thread in threads:
    print(thread['name'])

# обновление данных

threads = list(threads_collection.find({"name": "мемы1"}))
for thread in threads:
    thread['name'] = "илосос"
    threads_collection.update({"_id": thread['_id']}, thread)

# удаление

threads_collection.remove({'name': 'мемы'})

