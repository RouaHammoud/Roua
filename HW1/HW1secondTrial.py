import numpy as np 
import matplotlib.pyplot as plt 

def Lagra(x):
    x0= x-1
    x1 = x+ 1
    f0= x0** 2 
    f1= x1**2
    return f0 * ((x-x1)/(x0-x1)) + f1 *((x- x0)/(x1- x0))
X= np.array(np.arange(-15, 16, 2))
Ydata=[]
Y= []
for i in X:
    Ydata.append(i**2+ 15 * np.random.randn())
    Y.append(Lagra(i))
ax= plt.axes()
ax.plot(X, Y)
ax.scatter(X, Ydata)
plt.show()

