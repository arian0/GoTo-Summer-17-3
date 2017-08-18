import random

from PIL import Image

# открываем картинку
img = Image.open("cat.jpg").convert("RGBA")
pixels = img.load()

# размеры
print(img.width, img.height)

#горы
mountains = Image.open("mountains.jpg")
mountains = mountains.resize((img.width, img.height))

for x in range(img.width):
    for y in range(img.height):
        r, g, b, tr = pixels[x, y]
        tr = 20
        a = (r+g+b)//3
        if a > 150:
            pixels[x, y] = (255,255,255, tr)
        else:
            pixels[x, y] = (170, 20, 50, tr)

        r, g, b, tr = pixels[x, y]
        r = max(0, min(255, r+random.randint(-125,125)))
        g = max(0, min(255, g+random.randint(-125,125)))
        b = max(0, min(255, b+random.randint(-125,125)))
        pixels[x, y] = (r,g,b, tr)

mountains.paste(img, (0,0) , img)
mountains.show()





