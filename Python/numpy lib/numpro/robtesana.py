#robot sensor data analyzer
#create sensor dataset with np.random
#inspect arrays (shape,ndim,dtype,size)
#index slice and iterate sensor readings
#compute per sensor statistics(mean,max)
#use searching np.argmax ,np.argmin and np.where
import numpy as np
arr=np.random.randint(0,100,size=(4,5))
print("Sensor Data:\n",arr)
print("--------------------------------------")
print("Array Shape:",arr.shape)
print("Array Dimensions:",arr.ndim)
print("Array Data Type:",arr.dtype)
print("Array Size:",arr.size)
print("--------------------------------------")
print("Slicing and Indexing:",arr[1:3,2:5])
print("Iterating Sensor Readings:")
for x in arr:
    for y in x:
        print(y)
print("--------------------------------------")
print("Mean Reading per Sensor:",np.mean(arr,axis=1))
print("Max Reading per Sensor:",np.max(arr,axis=0))
print("--------------------------------------")
print("Index of Sensor with Highest Reading per Timepoint:",np.argmax(arr,axis=0))
print("Index of Sensor with Lowest Reading per Timepoint:",np.argmin(arr,axis=0))
print("Index where Readings >80:\n",np.where(arr>80))