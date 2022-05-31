import numpy as np
a=np.array(['   a','b   '])
b=np.char.strip(a)
c=np.char.lstrip(a)
d=np.char.rstrip(a)
print(b)
print(c)
print(d)
