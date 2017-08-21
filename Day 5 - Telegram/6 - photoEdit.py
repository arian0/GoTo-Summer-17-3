import random
import uuid

import telebot
from PIL import Image

token = "338047813:AAGUqsnxgxyOeDRoNYe7SonpvEqxeHcrNpQ"

bot = telebot.TeleBot(token=token)

def process(path_to_file):
    img = Image.open(path_to_file)
    pixels = img.load()
    for i in range(img.width):
        for j in range(img.height):
            r,g,b = pixels[i,j]
            a = (r+g+b)//3
            pixels[i,j] = (a,a,a)
    img.save(path_to_file)


@bot.message_handler(content_types=['photo'])
def message_handler(message):
    # скачивание файла
    file_id = message.photo[-1].file_id
    path = bot.get_file(file_id)
    downloaded_file = bot.download_file(path.file_path)

    # узнаешь расширение и придумываем имя
    extn = '.' + str(path.file_path).split('.')[-1] # .jpg
    filename = str(uuid.uuid4()) + extn
    path_to_file = "images/" + filename
    print(path_to_file)

    # создаем файл и записываем туда данные
    with open(path_to_file, 'wb') as new_file:
        new_file.write(downloaded_file)

    # применяем фильтр
    process(path_to_file)

    # открываем файл и отправляем его пользователю
    with open(path_to_file, 'rb') as new_file:
        bot.send_photo(message.chat.id, new_file.read())





bot.polling(none_stop=True)