import numpy as np
import random

arr=np.random.rand(5)
print("Random Array(1D):\n",arr,"\n")

arr=np.random.rand(5,5)
print("Random Array(2D):\n",arr,"\n")

arr=np.random.randint(1,99,size=(5,5))
print("Random Array(2D int):\n",arr,"\n")

arr=np.random.randint(1,99,size=(2,5,2))
print("Random Array(3D int):\n",arr,"\n")