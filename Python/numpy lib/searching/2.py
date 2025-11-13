import numpy as np
arr=np.array([10,25,30,45,20,50,0])

print("Original array:",arr)
print("-----------------------------------")

x=np.where(arr>30)
print("Indexes where arr > 30:",x)
print("Value where arr > 30:",arr[x])
print("-----------------------------------")

max=np.argmax(arr)
print("Inde of maximum value:",max)
print("Maximum value:",arr[max])
print("-----------------------------------")

min=np.argmin(arr)
print("Inde of maximum value:",min)
print("Maximum value:",arr[min])
print("-----------------------------------")

arr1=np.array([10,20,30,40,50])
s=np.searchsorted(arr1,35)
print("Original array:",arr1)
print("Index where 35 should be inserted to keep order:",s)
print("-----------------------------------")

nz=np.nonzero(arr)
print("Indexes of non-zero elements:",nz)
print("Non-zero elements:",arr[nz])