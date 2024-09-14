# Join 1-d array

import numpy as np

'''arr1=np.array([1,2,3,4,5])

arr2=np.array([5,6,7,8,9,10])

arr=np.concatenate((arr1,arr2))
print(arr)'''


# Join 2d array
arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr=np.concatenate((arr1,arr2),axis=0)  # axis = 0 mean columns and 1 means rows
print(arr) 

#join 3-d array 
'''arr1= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
arr2= np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

arr=np.concatenate((arr1,arr2),axis=2)
print(arr)  '''