#  iterating using nditer function
import numpy as np

#arr=np.array([[[1,2,3,4],[6,7,8,9]],[[11,12,13,14],[15,16,17,18]]]) 
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
#arr=np.array([1,2,3,4,5],ndmin=5)

#for x  in np.nditer(arr):
for x  in np.nditer(arr[:, ::2]):
    print(x) 


'''for x  in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
    print(x) '''