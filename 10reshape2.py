import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)     # Cconverting 1 d array into 3d array with 2X2 elements

print(newarr) 