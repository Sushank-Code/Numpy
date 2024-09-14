import numpy as np                 # array indexing

q=[1,2,3,4,5]
arr = np.array(q)
print(arr[0])
print(arr[2]+arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10],[11,12,13,14,15]])  # --> 2-d array indexing
print(arr[2,2])

arr = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9], [10, 11, 12]]])
print(arr[1,1,1])