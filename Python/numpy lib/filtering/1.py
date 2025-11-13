# Filtering means extracting only specific elements
# from an array that satisfy a given condition 
# (like values greater than 20, even numbers, etc.).
# Filtering helps you analyze, clean, or process 
# only the data you need — just like filtering unwanted 
# sensor readings in robotics or removing outliers in data science.

# How Filtering Works
# You create a boolean condition → (True/False values)
# You apply that condition on the array → it returns only elements where condition is True.

import numpy as np
arr = np.array([10, 20, 30, 40, 50])
# Create a filter for numbers greater than 25
filter_arr = arr > 25
print("Filter Condition:", filter_arr)
print("Filtered Array:", arr[filter_arr])

# Explanation:
# The condition arr > 25 checks each element.
# It keeps only elements where condition is True → 30, 40, 50.


# Example 2: Filter Even Numbers
arr = np.array([1, 2, 3, 4, 5, 6])
filter_arr = arr % 2 == 0
print("Even Numbers:", arr[filter_arr])


# Example 3: Manual Filter Creation
# You can manually define a filter list of True/False:
arr = np.array([10, 20, 30, 40])
filter_arr = [True, False, True, False]
print("Filtered Array:", arr[filter_arr])