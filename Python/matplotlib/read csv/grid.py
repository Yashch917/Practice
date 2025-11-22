import numpy as np
import matplotlib.pyplot as plt

x=np.array([3,8,1,10])
y=np.array([1,6,4,2])
plt.plot(x)
plt.plot(y)
plt.xlabel("People")
plt.ylabel("Scores")
plt.title("People vs Scores")
plt.grid(axis='y',color='gray',linestyle='--',linewidth=0.5)
plt.show()