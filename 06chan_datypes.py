import numpy as np
k=[1.1,1.45,1.6,1.7,1.9]
arr=np.array([k])

print("Before :",arr.dtype)

newarr=arr.astype('i')
# newarr=arr.astype(int)                    #other way for changing the data type

print("After changing data type:",newarr.dtype)