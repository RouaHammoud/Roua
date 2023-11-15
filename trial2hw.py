import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import scipy 
k, m= sp.symbols('k m')
N= 10
L= sp.Matrix.zeros(N,N)

for i in range(N):
    if i == 0:
        L[i, i] = -1 *(k/m)
        L[i, i+1]= 1 *(k/m)
    elif i==N-1:
        L[i , i]= -1 * (k/m)
        L[i, i-1]= 1 * (k/m)
    else:
        L[i , i] = -2 * (k/m)
        L[i, i-1]= 1 * (k/m)
        L[i, i+1]= 1 *(k/m)

L_prime= - L
#print(values)
eigenvalues = L_prime.eigenvals()

# Check if any eigenvalue is close to 0 within a tolerance

eigenvectors= L.eigenvects(0)
print(eigenvectors)
