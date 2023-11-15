import numpy as np
import matplotlib.pyplot as plt
from sympy import re, im, I, E, symbols, diff
import sympy as sp
x, y = symbols('x y', real=True)
z= x + I * y
def f(z):
    return z**3 -3
z0= 0.5 + I * 2
z_list= [z0]
def df(z, f):
    f_real = re(f(z))
    f_imag = im(f(z))
    # Calculate the partial derivatives
    df_dx = diff(f_real, x) + I * diff(f_imag, x)
    df_dy = diff(f_real, y) + I * diff(f_imag, y)
    return df_dx + df_dy 
for i in range(20):
    z= z0 - f(z0)/df(z0, f(z0))
    z_list.append(z)
    z0= z
print(z_list)

