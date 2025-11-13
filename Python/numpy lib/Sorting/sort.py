#Sorting Arrays:
#Sorting means putting eleements in an ordered sequence.
#Ordered sequence is any sequence that has an
#order coressponding to elements, like numeric
#or alphabetical, ascending or descending.
#The Numpy ndarray object has a function called sort()
#that will sort a specified array

import numpy as np
arr=np.array([15,5,67,56,89,23,34,2,5])
print("Original array:",arr)
print("Sorted array:",np.sort(arr))