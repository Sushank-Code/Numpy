# copy vs view

import numpy as np

arr=np.array([1,2,4,6,7])

#k=arr.copy()                    #copy { should not affect the original array }
k=arr.view()                   #view { should affect the original array }

#arr[0]=45     #change made to the original array
k[0]=31        #change made to the view

print(arr)
print(k)