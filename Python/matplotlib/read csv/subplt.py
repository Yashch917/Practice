import numpy as np
import matplotlib.pyplot as plt

x=np.array([35,25,25,15])
y=np.array([2,5,4,11])

plt.subplot(3,1,1)
plt.bar(y,x,color='purple')
plt.grid()
plt.title('Bar Chart')
plt.xlabel('X axis')
plt.ylabel('Y axis')

plt.subplot(3,1,2)
plt.scatter(y,x,color='orange')
plt.title('Scatter Plot')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.tight_layout()

plt.subplot(3,1,3)
x=np.array([35,25,25,15])
y=['Apple','Banana','Cherry','Date']
c=['#ff9999','#66b3ff','#99ff99','#ffcc99']
ex=(0.1,0.2,0.3,0)
plt.pie(x,labels=y,autopct='%1.1f%%',colors=c,explode=ex,shadow=True)
plt.legend(title="Fruits",loc="best")
plt.show()