import numpy as np
import matplotlib.pyplot as plt

x=np.array([3,8,1,10])
y=np.array([1,6,4,2])
plt.plot(x,linestyle='dotted',marker='o',color='red')
plt.plot(y,linestyle='dashed',c='#4CAF50',marker='x',linewidth=10)
plt.show()