import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x= sp.symbols('x')
def f(x):
    return ((1.1926 * 10**(-16))/x**5) * (1/(sp.exp((4.5*10**(-5))/x)-1))
x0 =0.002
f_x0= f(x0)
df = sp.diff(f(x))
x1= x0 - f_x0/ df.subs(x, x0).evalf()
tol= 10**(-10000)
def root(x0, x1, f_x0, df, tol):
    while abs(x1-x0)>=tol:
        x0= x1
        f_x0= f(x0)
        x1= x0 - (f_x0/ df.subs(x, x0).evalf())
    return x1

print(root(x0, x1, f_x0, df, tol))