# import urllib.request
from PIL import Image

# url = 'http://www.pythonchallenge.com/pc/def/oxygen.png'
# urllib.request.urlretrieve(url, 'image.png')

img = Image.open('image.png')

width = img.width
height = img.height
pix = [[] for i in range(width)]
for i in range(width):
    for j in range(height):
        pix[i].append(img.getpixel((i, j)))

row = [el[48][1] for el in pix]
print(row)
out = [chr(el) for el in row]
string = ''.join(out).split()
print(string)