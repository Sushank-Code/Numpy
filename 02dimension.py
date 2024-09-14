# 0-D , 1-D , 2-D , 3-D arrays

import numpy as np
arr= np.array(42)      # -> 0-D
arr= np.array([1,2,3])   # -> 1-D  
arr= np.array([[1,2,3],[1,2,3]])  # -> 2-D 
arr= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])  # -> 3-D = contain two 2-D array
print(arr)

'''arr = np.array([1,2,3],ndmin=5)        # creating many dimension array using ndim
print(arr)

print(arr.ndim)                       # Finding the dimension of array
'''