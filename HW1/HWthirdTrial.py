import numpy as np
import matplotlib.pyplot as plt 
X= np.linspace(-15, 15, 1000)
Y= np.array([(i**2 + np.random.rand()) for i in X])
x= 0.9
n= len(X) -1 
Y2=[]
for i in range(0, n):
    for j in range(0, n-i):
        Y2.append((x - X[j])/(X[i + j + 1]- X[j])* Y[j +1] + ((x - X[i+j+1])/ (X[j] - X[i+j+1])) * Y[j])
print(Y2[0])