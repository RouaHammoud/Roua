import numpy as np
import matplotlib.pyplot as plt 
from math import cos

#Runge_kutta 2
x0=3 
v0=0
h= np.linspace(0.1, 2, 20)
print(h)
w=2
w_p= 1.41 * w
f=1.41
t=[] 
X=[]
V=[]
V2=[]
X1=[]
ERROR=[]
for i in range(len(h)):
    t.append(list(np.arange(0, 10, h[i])))
    X.append([3* (1-cos(w * j)) for j in t[i]])
    v1=[v0]
    v2=[v0]
    v3=[v0]
    v4=[v0]
    x=[x0]
    error=[]
    for k in range(1, len(t[i])):
        v1.append(v1[k-1] + (h[i]/2) * (f * cos(w_p * (t[i][k-1] + h[i]/4))) - w**2 * x[k-1])
        v2.append(v2[k-1] + (h[i]) * (f * cos(w_p * (t[i][k-1] + h[i]/2))) - w**2 * x[k-1])
        x.append(x[k-1]+ (1/6) * (v1[k] + 3 * v2[k]))
        error.append(x[k-1]- X[i][k-1])
    V.append(v1)
    V2.append(v2)
    X1.append(x)
    ERROR.append(abs(sum(error)))
plt.plot(h, ERROR, color= 'r', label= 'error')
plt.xlabel('h')
plt.ylabel('Error')
plt.title('RK4 Method Error for different intervals of time')
plt.grid()
plt.show()