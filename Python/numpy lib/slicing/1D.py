import numpy as np
#--------------------Slicing---------------------
arr4=np.array([0,1,2,3,4,5,6,7,8,9])
print("Array for Slicing:")
print(arr4)
print("Slicing 2:9  ", arr4[2:9])
print("Slicing  :3  ", arr4[:3])
print("Slicing 5:   ", arr4[5:])
print("Slicing  ::2 ", arr4[::2])