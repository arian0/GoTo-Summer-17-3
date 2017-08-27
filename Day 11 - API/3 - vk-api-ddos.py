# token - https://oauth.vk.com/authorize?client_id=6163289&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=friends,photos ,audio,video,docs,notes,pages,status,wall,groups,messages,notifications,offline&response_type=token
# docs - https://vk.com/dev/manuals
# vk - https://pikabu.ru/story/api_vkontakte_dlya_python_3961240
import json
import requests

# задаем адрес, токен, метод, версию и параметры
token = "PASTE YOUR TOKEN HERE"
url = "https://api.vk.com/method/{method}?{params}&access_token={token}&v={version}"
method = "wall.post"
v = 5.68
params = "owner_id=236381200&message=vk api ddos&attachments=photo7980360_456239990"

for i in range(10):
    response = requests.get(url.format(method=method, version=v, params=params, token=token))
    print(response.json())