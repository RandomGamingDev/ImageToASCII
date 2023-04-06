from PIL import Image

chars = []
with open("chars.txt") as file:
    chars = [char.rstrip() for char in file.readlines()]

img = Image.open(str(input("Enter the name of the image that you would like to conver to ASCII: "))).resize((
    int(input("Enter the x resolution of the image: ")),
    int(input("Enter the y resolution of the image: "))
), resample=Image.Resampling.BILINEAR)
img = img.rotate(90, expand = 1)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixel = img.getpixel((x, y))
        value = 0
        for color in pixel:
            value += color
        print(chars[round((value / (255 * len(pixel))) * len(chars)) - 1], end='')
    print()
