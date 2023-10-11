import numpy as np 
from scipy import integrate
from scipy import misc
import matplotlib.pyplot as plt
intervals= [0.2, 0.4, 0.6, 0.8, 1, 2, 3, 5, 7, 8, 10]
list_of_X= [np.arange(0, 100, i) for i in intervals]
def Simpson(X, h):
    Y= np.array([1/(i**2 + 1) for i in X])
    odd =0
    for o in range(1, len(X)-1, 2):
       odd += Y[o]
    odd = 4 * odd

    even=0
    for e in range(2, len(X)-2, 2):
        even += Y[e]
    even = 2 * even 

    integral= ((Y[0] + odd + even + Y[-1]) * h)/3
    return integral
Integrals=[]
error=[]
def f(x):
    y= (1/(1+x**2))
    return y
for i in list_of_X:
    h= i[1] -i[0]
    Integrals.append(Simpson(i, h))
    c= (i[-1] +i[0])/2
    fourth_derivative= misc.derivative(f,c,dx=h, args=(),n=4, order=5)
    error.append(abs(-((i[-1]-i[0])/180)*h**4 * fourth_derivative))
print(Integrals)
machine=[]
for i in range(len(list_of_X)):
    Y= np.array([1/(j**2 + 1) for j in list_of_X[i]])
    machine.append(integrate.simpson(Y, list_of_X[i], dx= list_of_X[i][1]-list_of_X[i][0]))
error2=[]
for i in range(len(Integrals)):
   error2.append(abs(Integrals[i]- machine[i] ))
print(machine)
plt.figure()
plt.scatter(intervals, error)
plt.show()
plt.figure()
plt.scatter(intervals, error2)
plt.show()