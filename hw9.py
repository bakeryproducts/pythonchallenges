import numpy as np
import matplotlib.pyplot as plt
import random
x = np.linspace(0,5)

y = np.cos(x)
f = np.exp(-x)*np.sin(4*x)
g = np.exp(-x)*np.cos(4*x)

plt.plot(x,f,'r',linewidth=5,label='$ e^{-x} \sin(4x) $')
plt.plot(x,g,'b',label='$ e^{-x} cos(4x) $')
plt.ylabel('f')
plt.xlabel('x')
plt.title('HW9 at apmonitor.com')
plt.legend()
#plt.show()

x = np.linspace(0,10,10)
y1=x
y2=x**2
y3=x**3
y4=x**.5

plt.figure()
plt.subplot(2,2,1)
plt.plot(x,y1,'ro')
plt.title('i am function 1')

plt.subplot(2,2,2)
plt.plot(x,y2,'g--')
plt.title('i am function 2')


plt.subplot(2,2,3)
plt.plot(x,y3,'b^')
plt.title('i am function 3')

plt.subplot(2,2,4)
plt.plot(x,y4,'ks')
plt.title('i am function 4')

#plt.savefig('foo.png', bbox_inches='tight')
#plt.show()

plt.figure()
x = np.arange(0,100)
y = np.zeros(x.size)
z = np.zeros(x.size)

for i in range(x.size):
    y[i] = 2* x[i] + 50*random.random()
    z[i] =250* random.random() -2*x[i]

plt.plot(x,y,'ro',markersize=3)
plt.plot(x,z,'bs')
plt.xlim(0,50)
plt.ylim(0,200)
#plt.axes([0,0,10,10])

plt.show()

#print(a)