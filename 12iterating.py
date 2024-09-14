# Iterating 

import numpy as np

#arr=np.array([1,2,3,4,5,6,7,8])    # 1-d array
#arr=np.array([[1,2,3],[5,6,7]])    # 2-d array
arr=np.array([[[1,2,3,4],[6,7,8,9]],[[11,12,13,14],[15,16,17,18]]])      #3d array
#arr=np.array([1,2,3,4,5],ndmin=5)                 # n dimension array

for x  in arr:
    print(x)