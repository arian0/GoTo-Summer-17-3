from PIL import Image


def invert(im):
    pixels = im.load()
    for x in range(im.width):
        for y in range(im.height):
            r, g, b = pixels[x, y]
            r = 255 - r
            g = 255 - g
            b = 255 - b
            pixels[x, y] = (r, g, b)
    return im


# открываем картинку
img = Image.open("cat.jpg")

cat = img.crop([img.width // 5, img.height // 5, 4 * img.width // 5, 4 * img.height // 5])
cat_small = img.crop([img.width // 3, img.height // 3, 2 * img.width // 3, 2 * img.height // 3])

cat = invert(cat).transpose(Image.FLIP_LEFT_RIGHT)
img.paste(cat, [img.width // 5, img.height // 5])
img.paste(cat_small, [img.width // 3, img.height // 3])



img.show()
