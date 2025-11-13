import numpy as np
arr = np.array([
    [5, 15, 25],
    [35, 45, 10]
])

# Filter elements greater than 20
filter_arr = arr > 20
print("Filter Array:\n", filter_arr)
print("Filtered Values:", arr[filter_arr])