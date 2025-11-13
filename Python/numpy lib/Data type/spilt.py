#Array Spilting
#Definition
#Splitting means dividing one array into multiple sub-arrays.
#main functions:
#numpy.array_split()
#numpy.hsplit()
#numpy.vsplit()

import numpy as np
arr= np.array([1,2,3,4,5,6])
parts= np.array_split(arr, 3)
print("Split arrays:", parts)

arr=np.array([[1,2,3,4],[5,6,7,8]])
parts=np.hsplit(arr,2)
print("Horizontally split arrays:",parts)

arr=np.array([[1,2,3,4],[5,6,7,8]])
parts=np.vsplit(arr,2)
print("Vertically split arrays:",parts)

arr1=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])