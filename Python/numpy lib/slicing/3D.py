import numpy as np
arr=np.array([
    [[1,2,3],
    [4,5,6],
    [7,8,9]],
      
    [[10,11,12],
    [13,14,15],
    [16,17,18]]
])

print("3D array:")
print(arr)
print("-----------------------------------")
print(arr[0])
print("-----------------------------------")
print(arr[1])
print("-----------------------------------")
print("Slice rows 0:2 and columns 1:3")
print(arr[0:2,0:2,1:3])