import json

with open('data.json') as file:
    threads = json.loads(file.read())
print(len(threads))