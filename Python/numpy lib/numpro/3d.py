#Create a 3d array having 2 layers and iterarting each layer of each row and column one by one and print dimension ndim
import numpy as np
arr=np.random.randint(0,100,size=(2,3,4))
print("3D Array:\n",arr)
print("Array Dimension:",np.ndim(arr))
for x in arr:
    for y in x:
        for z in y:
            print(z)