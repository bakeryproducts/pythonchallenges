#challenge 11 : http://www.pythonchallenge.com/pc/return/5808.html one with double image 8/2/17
#import urllib.request
from PIL import Image
import scipy.misc as smp

#url = 'http://www.pythonchallenge.com/pc/return/cave.jpg'
#urllib.request.urlretrieve(url,'image11.jpg')

img = Image.open('cave.jpg')
width = img.width
height = img.height

pix = list(img.getdata())
# image1pix = [[pix[i+j*width] for i in range(0,width,2)] for j in range(0,height,2)]
# image1 = smp.toimage(image1pix)

image2pix = [[pix[i+j*width] for i in range(1,width,2)] for j in range(1,height,2)]
image2 = smp.toimage(image2pix)

image2.show()
