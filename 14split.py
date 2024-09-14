# sPlit 

import numpy as np
arr = np.array([1, 2, 3, 4, 5])

# newarr=np.array_split(arr,2)       # split into 2 arrays
newarr=np.array_split(arr,3)         # split into 3 arrays 

print(newarr)

print(newarr[0])
print(newarr[1])
print(newarr[2])