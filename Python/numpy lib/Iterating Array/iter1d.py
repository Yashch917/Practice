# Iterating Arrays
# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, 
# we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through 
# each element one by one.
# “We iterate through NumPy arrays when we want 
# to look at each value and do something with it.”
# Example:
# Iterate on the elements of the following 1-D array:
import numpy as np
import random
arr=np.random.randint(0,100,size=5)
print("Iterating 1D Array:")
for x in arr:
    print(x)
# Explanation:
# A 1D array has elements in a single line.
# The loop goes element by element: 10 → 20 → 30 → 40 → 50.