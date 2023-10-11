import numpy as np
import matplotlib.pyplot as plt 
from scipy import integrate
from scipy.interpolate import CubicSpline

def Trapezoid(X, h):
    Y= np.array([1/(i**2 + 1) for i in X])
    integral=0
    pair= 0
    for j in range(len(X)-1):
        pair= (Y[j] + Y[j+1]) * (h)/2
        integral += pair
    return integral
intervals= [0.2, 0.4, 0.6, 0.8, 1, 2, 3, 5, 7, 8, 10]
list_of_X= [np.arange(0, 100, i) for i in intervals]
x = [1, 10, 20, 25]
def CubicSpline(x, X):
    y= [1/(1+i**2) for i in x]
    n= len(x) 
    z= np.zeros(n)
    z[0]= 0
    for i in range(0, n-1):
       z[i+1]= - z[i] +2 * ((y[i+1]-y[i])/(x[i+1]-x[i]))
    Y=[]
    S=0
    for i in X:
      for j in range(n-1):
        if i <= x[j+1] and i>= x[j]:
           S= y[j] + z[j] *(i- x[j]) + ((z[j+1]-z[j])/(x[j+1]-x[j])) * ((i-x[j])**2/2)
           Y.append(S)
           break
      S=0
    return Y
def Trapezoid2(X, h):
    Y= CubicSpline(x, X)
    integral=0
    pair= 0  
    for j in range(len(X)-1):
        pair= (Y[j] + Y[j+1])* (h/2)
        integral += pair
    return integral
Integrals=[]
error=[]
Integrals2=[]
for i in list_of_X:
    h= i[1] -i[0]
    Integrals.append(Trapezoid(i, h))
    print(len(i))
    print(len(CubicSpline(x, i)))
    #Integrals2.append(Trapezoid2(i, h))
    c= (i[-1] +i[0])/2
    second_derivative= (2*(c**2+1)**2 - 8 * c**2 * (c**2+1))/(c**2+1)**4
    error.append(-((i[-1]-i[0])/12)*h * second_derivative)
print(Integrals)
#print(Integrals2)

machine=[]
for i in range(len(list_of_X)):
    Y= np.array([1/(j**2 + 1) for j in list_of_X[i]])
    machine.append(integrate.trapezoid(Y, list_of_X[i], dx= list_of_X[i][1]-list_of_X[i][0]))
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
