import numpy as np

#arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
arr=np.array([[1,3,4,5],[10,12,13,4]])

newarr= np.array_split(arr,2)                 # 2 d array is split into two 2d array
print(newarr)