import numpy as np 
import matplotlib.pyplot as plt 
np.random.seed(42)
X= np.linspace(-4, 100, 20)
Y= np.random.choice(np.arange(-7, 100), 20)
def linear_regression(n, X, x):
    b=n
    matrix=[]
    for i in range(len(X)):
        b=n
        while b >=0:
          matrix.append(X[i]**b)
          b= b-1
        
    matrix= np.reshape(matrix, (len(X), n+1))
    transpose= matrix.T
    product= transpose @ matrix 
    inverse= np.linalg.inv(product)
    final= inverse @ transpose @ Y
    matrix1=[]
    b=n
    for i in range(len(x)):
        b=n
        while b >=0:
          matrix1.append(x[i]**b)
          b= b-1
        
    matrix1= np.reshape(matrix1, (len(x), n+1))
    y= matrix1 @ final
    return y
x= np.linspace(1, 100, 200)
Y1= np.random.choice(np.arange(100), 200)
plt.figure()
plt.plot(x, linear_regression(3, X, x), label= "The fit")
plt.scatter(X, Y, color= 'red')
plt.show()
list_of_orders=[1, 2, 3, 4, 5, 6, 7]
error1= []
error2=[]
x1 = x[:int(0.8 * len(x))]
x2 = x[int(0.8 * len(x)):]
y1 = Y1[:int(0.8 * len(Y1))]
y2 = Y1[int(0.8 * len(Y1)):]
for i in list_of_orders:
   error1.append(sum((linear_regression(i, X, x1)- y1)**2 ))
   error2.append(sum((linear_regression(i, X, x2)- y2)**2 ))
plt.figure()
plt.plot(list_of_orders, error1, label= 'Training Error')
plt.plot(list_of_orders, error2, color= 'red', label= 'Testing Error')
plt.show()





 