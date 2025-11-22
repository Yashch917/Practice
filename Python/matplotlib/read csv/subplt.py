#rotate the layers of subplot in interval 0f 2 seconds
import numpy as np
import matplotlib.pyplot as plt

x=np.array([35,25,25,15])
y=np.array([2,5,4,7])
plt.fill_between(x,y,alpha=0.5,color='lightblue')

plt.subplot(2,2,1)
plt.bar(y,x,color='purple')
plt.grid()
plt.title('Bar Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.subplot(2,2,2)
plt.scatter(y,x,color='orange')
plt.title('Scatter Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.tight_layout()

plt.subplot(2,2,3)
c=['#ff9999','#66b3ff','#99ff99','#ffcc99']
ex=(0.1,0.2,0.3,0)
plt.pie(x,labels=y,autopct='%1.1f%%',colors=c,explode=ex,shadow=True)
plt.legend(title="Fruits",loc="best")

plt.subplot(2,2,4)
plt.plot(x,linestyle='dotted',marker='o',color='red')
plt.plot(y,linestyle='dashed',c='#4CAF50',marker='x',linewidth=10)
plt.show()