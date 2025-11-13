#Array Reshaping
#Reshaping means changing the number of
#rows and columns of an array without changing actual data
#Convert arrays between 1D, 2D, and 3D Formats
#Rule of Reshaping
#arr=np.array([1,2,3,4,5,6])
#arr has 6 elements
#arr.reshape(3,2)  3*2=6
#arr.reshape(2,3)  2*3=6
#arr.reshape(4,2)  4*2=8
#If elements dont match , it gives:
#ValueError: cannot reshape array of size into shape(4,2)

import numpy as np
arr=np.array([1,2,3,4,5,6])
narr=arr.reshape(2,3)
print("Original Array:")
print(arr,"\n")
print("Reshaped Array:")
print(narr,"\n")
print("------------------------------------------------")

narr=arr.reshape(3,-1)
print("Original Array:")
print(arr,"\n")
print("Reshaped Array:")
print(narr,"\n")
print("------------------------------------------------")

arr1=np.array([1,2,3,4,5,6,7,8])
narr=arr1.reshape(2,2,2)
print("Original Array:")
print(arr1,"\n")
print("Reshaped Array:")
print(narr,"\n")
print("------------------------------------------------")

arr2=np.array([[1,2,3,4],[5,6,7,8]])
narr=arr2.flatten()
print("Original Array:")
print(arr2,"\n")
print("Reshaped Array:")
print(narr,"\n")
