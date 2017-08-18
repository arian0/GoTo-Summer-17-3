from PIL import Image

# открываем картинку
img = Image.open("cat.jpg")
pixels = img.load()

# размеры
print(img.width, img.height)

for x in range(img.width):
    for y in range(img.height):
        r, g, b = pixels[x, y]
        r = min(r + 200, 255)
        g = min(g + 100, 255)
        b = min(b + 100, 255)
        pixels[x, y] = (r, g, b)

img.show()
