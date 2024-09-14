import numpy as np

#arr=np.array([[1,2,3],[5,6,7]])  
arr=np.array([[[1,2,3,4],[6,7,8,9]],[[11,12,13,14],[15,16,17,18]]])  

for x in arr:
    for y in x:
        print(y)
       

for x in arr:
    for y in x:
        for z in y:
            print(z)
       

