#create a array of 20 elements apply view method then update any 3 elements with random module of any index then print both arrays
import numpy as np
import random
arr=np.random.randint(1,21,size=20)
print("Original Array:",arr)
arr1=arr.view()
print("View Array:",arr1)
for _ in range(3):
    index=random.randint(0,19)
    new_value=random.randint(1000,2000)
    arr1[index]=new_value
print("After Updating 3 elements in View Array")
print("Original Array:",arr)
print("View Array:",arr1)
