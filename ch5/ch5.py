import requests
import pickle
from urllib.request import urlopen

url = 'http://www.pythonchallenge.com/pc/def/banner.p'

raw = urlopen(url).read()

dat = pickle.load(urlopen(url))

for i in range(len(dat)):
    for j in range(len(dat[i])):
        print(dat[i][j][0] * dat[i][j][1],end='')
    print()