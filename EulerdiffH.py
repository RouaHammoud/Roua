import numpy as np
import matplotlib.pyplot as plt
from math import cos

x0= 3
v0 = 0 

#main function
h= np.linspace(0.1, 1, 20)
print(h)
w=2
t=[] 
X=[]
V=[]
X1=[]
ERROR=[]
for i in range(len(h)):
    t.append(list(np.arange(0, 10, h[i])))
    X.append([3* cos(w * j) for j in t[i]])
    v=[v0]
    x=[x0]
    error=[]
    for k in range(1, len(t[i])):
        v.append(v[k-1] - w**2 * x[k-1] * h[i])
        x.append(x[k-1] + v[k-1] * h[i])
        error.append(x[k-1]- X[i][k-1])
    V.append(v)
    X1.append(x)
    ERROR.append(abs(sum(error)))
print(ERROR)
plt.plot(h, ERROR, color= 'r', label= 'error')
plt.xlabel('h')
plt.ylabel('Error')
plt.title('Euler Method Error for different intervals of time')
plt.grid()
plt.show()