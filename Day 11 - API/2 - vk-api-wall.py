# token - https://oauth.vk.com/authorize?client_id=6163289&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token
# docs - https://vk.com/dev/manuals
# vk - https://pikabu.ru/story/api_vkontakte_dlya_python_3961240
import json
import requests

# задаем адрес, токен, метод, версию и параметры
token = "PASTE YOUR TOKEN HERE!!!"
url = "https://api.vk.com/method/{method}?{params}&access_token={token}&v={version}"
method = "wall.get"
v = 5.68
params = "domain=baneks&count=100&offset={0}"

# делаем первый запрос, чтобы узнать количество
response = requests.get(url.format(method=method, version=v, params=params.format(0), token=token))
result = response.json()

# узнаем количество
count = result['response']['count']
print('count = {}'.format(count))

# скачиваем посты с шагом i (используем i, как отступ - offset)
items = []
for i in range(0, count, 100):
    print("downloading - {}".format(i))
    response = requests.get(url.format(method=method, version=v, params=params.format(i), token=token))
    result = response.json()
    count = result['response']['count']
    items += result['response']['items']

# сортируем
items = sorted(items, key=lambda x: x['likes']['count'], reverse=True)

# сохраняем на будущее
with open('aneks.json', 'w') as file:
    file.write(json.dumps(items))

# выводим самые топовые
for item in items[:100]:
    print(item['text'])
    print(item['likes']['count'])
    print('--' * 10)



