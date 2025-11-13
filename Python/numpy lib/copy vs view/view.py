import numpy as np
arr=np.array([1,2,3,4,5])
arr1=arr.view()
print("Original Array:",arr)
print("Copied Array:",arr1)
arr1[0]=99
print("After Updating first element of Second array")
print("Original Array:",arr)
print("Copied Array:",arr1)