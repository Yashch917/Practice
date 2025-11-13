import numpy as np
import random
arr=np.random.randint(0,100,size=(5,2))
print("Iterating 2D Array:")
for x in arr:
    for y in x:
        print(y)