from PIL import Image

# открываем картинку
img = Image.open("cat.jpg")
pixels = img.load()

# размеры
print(img.width, img.height)

for x in range(img.width):
    for y in range(img.height):
        r, g, b = pixels[x, y]
        r = 255 - r
        b = 255 - b
        g = 255 - g

        pixels[x, y] = (r, g, b)

img.show()
