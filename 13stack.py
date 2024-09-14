import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.stack((arr1, arr2), axis=0)
print(arr)
'''arr_c = np.concatenate((arr1, arr2))
print(arr_c) '''

#arr = np.vstack((arr1, arr2))               # along the vertically
#arr = np.hstack((arr1, arr2))               # along the horizontally
#arr = np.dstack((arr1, arr2))               # along the height

 
