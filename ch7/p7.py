# challenge 7 at http://www.pythonchallenge.com/pc/def/oxygen.html 07/02/17

from PIL import Image
import re

# import urllib.request
# url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
# urllib.request.urlretrieve(url, 'image.png')

img = Image.open('image.png')
width = img.width
height = img.height
pixels = [[] for i in range(width)]
# pls rewrite this double loop python style
for i in range(width):
    for j in range(height):
        pixels[i].append(img.getpixel((i, j)))

row = [element[48][1] for element in pixels][::7]  # 48 is middle line with code encrypted in it, blocks of code each approx 7 pxls wide
# print(row)

# out = [chr(el) for el in row]
message = ''.join(map(chr, row))
nums = re.findall('\d+', message)
result = ''.join(map(chr, map(int, nums)))
print(result)
