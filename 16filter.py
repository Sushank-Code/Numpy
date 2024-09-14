# Filter = creating a new array by getting elements out of an existing array

import numpy as np

arr=np.array([12,1,13,14])

'''x=[True,False,True,True]
newarr=arr[x]
print(newarr) '''

'''y=[]
for i in arr:
    if(i>12):
        y.append(True)
    else:
        y.append(False)
new=arr[y]
print(y)
print(new) '''

y=arr>12                            # shortcut
new=arr[y]
print(y)
print(new)