# challenge 12 http://www.pythonchallenge.com/pc/return/evil.html 9/2/17

file = open('evil2.gfx', 'rb')
data = file.read()
file.close()
for i in range(5):
    open(str(i) + '.jpg', 'wb').write(data[i::5])
