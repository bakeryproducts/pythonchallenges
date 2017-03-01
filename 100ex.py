import numpy as np

print(np.__version__)

a = np.zeros(10, dtype='int32')

a[4] = 1

mems = a.itemsize * a.size

b = np.random.randint(10, 49, 10)
b = np.arange(10, 50)

x = b[::-1]

mat = np.arange(0, 9).reshape(3, 3)

x = [1, 2, 0, 0, 4, 0]
nz = np.nonzero(x)

idm = np.identity(3)
idm2 = np.eye(3)

rv3 = np.random.rand(27).reshape(3, 3, 3)
rv32 = np.random.random((3, 3, 3))

rv10 = np.random.rand(100).reshape(10, 10)
rv102 = np.random.random((10, 10))
rv10min = np.min(rv10)
rv10max = np.max(rv10)
r102max, r102min = rv102.max(), rv102.min()

r30 = np.random.rand(30)

r30m = r30.mean()

br = np.ones((5, 5))
br[1:-1, 1:-1] = 0

br = np.pad(br, pad_width=1, mode='constant', constant_values=0)

# print(0 * np.nan)
# print(np.nan == np.nan)
# print(np.inf > np.nan)
# print(np.nan - np.nan)
# print(0.3 == 3 * 0.1)

z = np.diag(1 + np.arange(4), k=-1)  # k = offset of diagonal

chkb = np.zeros(64).reshape(8, 8)
chkb[::2, ::2] = 1
chkb[1::2, 1::2] = 1

tmp = np.unravel_index(100, (6, 7, 8))

z= np.tile(np.array([[0,1],[1,0]]),(4,3))       # tile func
#print(z)

a = 5*np.random.random((5,5))

a=(a-a.min())/(a.max()-a.min())
print(a)

color = np.dtype([  ('r',np.ubyte,1),
                    ('g',np.ubyte,1),
                    ('b',np.ubyte,1),
                    ('a',np.ubyte,1),
                  ])


a = np.random.random((5,3))
b=np.random.random((3,2))
c = a.dot(b)
print(c)
c=a@b
print(c)


