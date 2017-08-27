import requests

response = requests.get('http://roctbb.ru')

print(response.text)