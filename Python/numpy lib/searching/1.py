#Searching Arrays
#Searching means finding the position (index)
#of specific elements or checking conditions inside an array

import numpy as np
arr=np.array([1,2,3,4,2,4,5,6,5])
x=np.where(arr==2)
print(x)

#the example above will return a tuple: (array([1, 4]),)
#Which means that the value 2 is present at index 1,4

arr=np.array([1,2,3,4,5,6,7,8])
x=np.where(arr%2==0)
print(x)

arr=np.array([10,20,30,40])
x=np.searchsorted(arr,25)
print(arr)
print("25 should be inserted at index:",x)

marks=np.array([78,95,62,85,70])
s=np.sort(marks)
t=np.where(marks==np.max(marks))
print("Marks:",marks)
print("Sorted marks:",s)
print("Highest marks at index:",t)