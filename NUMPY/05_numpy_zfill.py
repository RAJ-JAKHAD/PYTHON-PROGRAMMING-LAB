import numpy as np
a=np.array([1,288,3999,99994],dtype=str)
b=np.char.zfill(a,5)
print(b)
