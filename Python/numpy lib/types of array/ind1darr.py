import numpy as np
arr=np.array([1,2,3,4,5])
print("1D array:",arr)
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])

try:
    print(arr[8])
except Exception as e:
    print("Error:", e)