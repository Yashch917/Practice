#Q.1 1D Array containing 5 elements and accessing 4th element
#Q.2 1D Array containing 20 elements and accessing any 7 elements
#Q.3 1D array slicing 10 elements 1:8, 4:7, 5:10

#--------------------Q.1--------------------
import numpy as np
arr=np.array([1,2,3,4,5])
print("1D array:")
print(arr)
print("4th element:", arr[3])
print("-------------------------------------------")

#--------------------Q.2--------------------
arr2=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
print("1D array with 20 elements:")
print(arr2)
print("Accessing 7 elements:")
for i in [0, 3, 5, 7, 10, 15, 19]:
    print(f"Element at index {i}: {arr2[i]}")
print("-------------------------------------------")

#--------------------Q.3--------------------
arr3=np.array([1,2,3,4,5,6,7,8,9,10])
print("1D array with 10 elements:")
print(arr3)
print("Slicing 1:8:", arr3[1:8])
print("Slicing 4:7:", arr3[4:7])
print("Slicing 5:10:", arr3[5:10])
print("-------------------------------------------")


