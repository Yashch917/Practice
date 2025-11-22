import numpy as np
import matplotlib.pyplot as plt

x=np.array([35,25,25,15])
y=['Apple','Banana','Cherry','Date']
c=['#ff9999','#66b3ff','#99ff99','#ffcc99']
ex=(0.1,0.2,0.3,0)
plt.pie(x,labels=y,autopct='%1.1f%%',colors=c,explode=ex,shadow=True)
plt.legend(title="Fruits",loc="best")
plt.show()