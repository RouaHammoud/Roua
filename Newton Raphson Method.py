import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

x= sp.symbols('x')
def f(x):
    return x**2 -3
x0 =3 
f_x0= f(x0)
df = sp.diff(f(x))
x1= x0 - f_x0/ df.subs(x, x0).evalf()

def root(x0, x1, f_x0, df):
    while round(x1, 3) != round(x0, 3):
         x0 = x1
         x1= x0 - (f_x0/ df.subs(x, x0).evalf())
    return x1

print(root(x0, x1, f_x0, df))










