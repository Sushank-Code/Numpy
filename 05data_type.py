# Data type
import numpy as np
#arr=np.array([1,2,4,5,6,7])
arr=np.array(['banana','game','hello'])

print(arr.dtype)                         # checking data type 

#k=np.array([1,2,3,4,5],dtype='f')        # defing the data type 
k=np.array([1,2,3,4,5],dtype='f8')        # defing the data type and we can give size as well
print(k)
print(k.dtype)