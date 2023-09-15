import numpy as np 
import matplotlib.pyplot as plt
xi = np.array([-10, -5,-2, 0, 2, 5, 10])
yi= np.array([1/(1 +i**2 ) for i in xi])
n= len(xi)-1
def Aitken_method(x, xi, yi,  start,n ):
    if start == n:
        return yi[start]
    else:
        L0= ((x- xi[n])/(xi[start] - xi[n]))
        L1= ((x- xi[start])/(xi[n] - xi[start]))
        return L0 * Aitken_method(x, xi, yi, start, n-1) + L1 * Aitken_method(x, xi, yi, start+1, n)

X= np.arange(-10, 10)
y = [Aitken_method(x, xi, yi, 0, n) for x in X]
Ydata= [1/(1+ i**2 ) for i in X]
plt.plot(X, y)
plt.scatter(xi, yi, color='red', label='Sample Points')
plt.plot(X, Ydata, linestyle='--', label='True Function')
plt.legend()
plt.show()
