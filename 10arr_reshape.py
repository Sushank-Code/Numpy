import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) 

#print(arr.reshape(4,3))                     #1-d array into 2-d array

print(arr.reshape(3,2,2))                    #1-d array into 3-d array

print(arr.reshape(-1))                      # Reshape into the original array