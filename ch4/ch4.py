import requests

n = '12345'
output = ''
for i in range(400):
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + n
    src_code = requests.get(url)
    text = src_code.text
    nl = '#' + str(i) + ' ' + text
    print(nl)
    n = text.split()[-1]
    output = output + nl + '\n'
    # print(n)

fw = open('ch4.txt', 'w')
fw.write(output)
print(output)
fw.close()
