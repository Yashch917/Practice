import numpy as np
import matplotlib.pyplot as plt

x=np.array([3,8,1,10])
y=np.array([1,6,4,2])
plt.plot(x,y,linestyle='dotted',marker='o',color='red')
plt.plot(y,linestyle='dashed',c='#4CAF50',marker='x',linewidth=10)

plt.fill_between(x,y,alpha=0.5,color='lightblue')

plt.show()