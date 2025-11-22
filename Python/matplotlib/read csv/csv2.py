import numpy as np
import matplotlib.pyplot as plt
points=np.array([5,6,9,7,1,8])
#for dotted line
plt.plot(points,linestyle='dotted')
#for histogram
plt.hist(points)
plt.show()