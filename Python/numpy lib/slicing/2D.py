import numpy as np
arr =np.array([[10,20,30],
               [40,50,60],
               [70,80,90]])
print("2D array:")
print(arr)
print("Accessing elements:")
print(arr[:1,1:3],"\n",arr[1:2,0:2],"\n",arr[2:3,1:3],"\n")
print("------------------------------------------")
print(arr[2,0:2])