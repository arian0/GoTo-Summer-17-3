import requests

response = requests.get("http://127.0.0.1:8888/notify?token=123&type=add&comment=blabla&amount=300")

answer = response.json()
print(response.status_code)
print(answer["result"])