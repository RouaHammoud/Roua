import numpy as np
import matplotlib.pyplot as plt 

#X= np.linspace(-2, 3, 2)
#n= len(X) -1 
#func=[]
#for i in X:
#   func.append(i**2 + np.random.randn())
n= 2
X= [-4, 0, 4]
Yi= []
for i in X:
    Yi.append(i**2 + np.random.rand())
def lagrange(x):
    sum_p=1
    sum_f=0
    for j in range(n+1):
        sum_p = 1
        for k in range (n+1):
            if k != j:
               sum_p *= (x - X[k])/ (X[j] - X[k])
        sum_f = sum_f + Yi[j] * sum_p
    return sum_f 
Y= []
x1= np.linspace(-4, 4, 50)
Y= np.array(lagrange(x1))
Ydata= np.array([i**2 + np.random.rand() for i in x1])
ax= plt.axes()
ax.plot(x1, Y)
ax.plot(x1, Ydata, linestyle= 'dotted')
plt.show()

 