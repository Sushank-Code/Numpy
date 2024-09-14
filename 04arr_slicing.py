import numpy as np                # array slicing

'''arr=np.array([1,2,3,4,5,6,7])
print(arr[1:5])
print(arr[-3:-1])
print(arr[1:5:2])'''

arr= np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(str(arr[1,1:4]))
print(arr[0:2,3])
print( arr[0:2,1:3]) #  ---> [0:2, 1:3] Here, 0:2 is array in arr (index) 