#Array Attributes (Properties of Arrays)
#Understand information about arrays such as:
#ndim -> number of dimensions
#shape -> number of rows and columns
#size -> total elements
#itemsize -> bytes per element

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("Dimensions:",a.ndim)
print("Shape:",a.shape)
print("Size:",a.size)
print("Item Size (in bytes):",a.itemsize)

#Array Reshaping
#Convert arrays between 1D, 2D, and 3D using reshape()
try:
    a1=np.array([1,2,3,4,5,6])
    reshaped=a1.reshape(4,2)
    print("Reshaped Array:",reshaped)
except Exception as e:
    print("Error:",e)
    
a=np.array([1,2,3])
b=np.array([4,5,6])
joined=np.concatenate((a,b))
print("Joined Array:",joined)

c=np.array([[1,2],[3,4]])
d=np.array([[5,6],[7,8]])
result=np.concatenate((c,d),axis=0)
print("Concatenated along rows:\n",result)

print("Concatenated along columns:\n",np.concatenate((c,d),axis=1))

e=np.array([1,2,3])
f=np.array([4,5,6])
result=np.hstack((e,f))
print("Horizontally Stacked:",result)

result=np.vstack((e,f))
print("Vertically Stacked:\n",result)