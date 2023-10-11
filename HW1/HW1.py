import numpy as np 
import matplotlib.pyplot as plt 
def function_quadratic(x):
    return x **2 
def Lagrangian_interpolation(x):
    n= 5
    m=4
    pol=0
    for i in range(m, n):
        if n - m== 1:
           pol += ((x- n) / (m- n)) * function_quadratic(i)
           n, m = m, n
        else: 
           j= i+ 1
           pol += ((x- j) / (j- i)) * function_quadratic(i)
    return pol
n= 5
X= np.linspace(-n ,n, 5)
Y= np.array(Lagrangian_interpolation(X))
Xdata = 15 * np.random.random(50)
ydata = function_quadratic(Xdata) + 0.1 * np.random.randn(50)
#0.1 * np.random... is the noise 
# Plot a 3-D line
# Fill in
ax= plt.axes()
# Data for three-dimensional scattered points
# Fill in
ax.plot(X, Y)
ax.scatter(ydata, Xdata)
plt.show()

