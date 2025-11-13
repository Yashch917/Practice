import numpy as np
import random
arr=np.random.randint(0,100,size=(2,5,2))
print("Iterating 3D Array:")
for x in arr:
    for y in x:
        for z in y:
            print(z)