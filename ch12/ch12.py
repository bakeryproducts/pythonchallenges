from PIL import Image
import scipy.misc as smp
img = Image.open('evil1.jpg')

width = img.width
height = img.height

pix = list(img.getdata())

data = [[pix[i+j*width] for i in range(width)] for j in range(0,height,2)]
image = smp.toimage(data)
image.show()