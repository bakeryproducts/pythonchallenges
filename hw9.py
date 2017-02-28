import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5)

y = np.cos(x)
f = np.exp(-x)*np.sin(4*x)
g = np.exp(-x)*np.cos(4*x)

plt.plot(x,f,'r',linewidth=5)
plt.plot(x,g,'b')
plt.ylabel('f')
plt.xlabel('x')
plt.title('HW9 at apmonitor.com')

plt.show()

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

plt.show()

#print(a)