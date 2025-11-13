import numpy as np
arr=np.array([1,2,3,4,5])
print("Data type:",arr.dtype)

arr1=np.array([1.5,2.3,3.8,9.9])
print("Data type:",arr1.dtype)

arr2=arr1.astype(int)
print(arr2)
print(arr2.dtype)