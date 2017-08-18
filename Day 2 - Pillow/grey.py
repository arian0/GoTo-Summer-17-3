from PIL import Image

# открываем картинку
img = Image.open("cat.jpg")
pixels = img.load()

# размеры
print(img.width, img.height)

for x in range(img.width//4):
    for y in range(img.height):
        r, g, b = pixels[x, y]

        a = (r+g+b)//3

        pixels[x, y] = (a, a, a)

for x in range(3*img.width//4, img.width):
    for y in range(img.height):
        r, g, b = pixels[x, y]

        a = (r+g+b)//3

        pixels[x, y] = (a, a, a)

img.show()
