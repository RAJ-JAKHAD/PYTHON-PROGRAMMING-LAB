import numpy as np
n=np.arange(4).reshape(2,2)
print(n)
print(np.amax(n))
print(np.amin(n))
# max and min along second axis:
print(np.amax(n,1))
print(np.amin(n,1))
