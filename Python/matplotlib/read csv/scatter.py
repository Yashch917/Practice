import numpy as np
import matplotlib.pyplot as plt

x=np.array([3,8,1,10])
y=np.array(['A','B','C','D'])

plt.scatter(x,y,c='green',edgecolor='black')
plt.xlabel("Count")
plt.ylabel("Section",rotation=0)
plt.title("Count vs Section")
plt.grid()
plt.show()