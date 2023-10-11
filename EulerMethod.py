import numpy as np
import matplotlib.pyplot as plt
from math import cos

x0= 3
v0 = 0 

#main function
h= 0.2
w=2
t= np.arange(0, 10, h)
X= np.array([3* cos(w * i) for i in t])

#Harmonic oscillator
v= [v0]
x=[x0]
for i in range(1, len(t)):
    v.append(v[i-1] - w**2 * x[i-1] * h)
    x.append(x[i-1] + v[i-1] * h)

error= np.array([x[i] -X[i] for i in range(len(t))])
plt.plot(t, x, label= 'Euler Approximation')
plt.plot(t, X, color= 'g', label= 'Original Function')
plt.plot(t, error, color= 'r', label= 'error')
plt.legend()
plt.show()