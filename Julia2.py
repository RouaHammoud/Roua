import numpy as np
from sympy import I, symbols

x, y = symbols('x y', real=True)
z = x + I * y

def f(z):
    return z**3 - 3   

def df(z, delta=1e-6):
    # Numerical approximation of the derivative
    df_dx = (f(z + delta) - f(z)) / delta
    df_dy = (f(z + I * delta) - f(z)) / delta
    return df_dx, df_dy

z0 = 0.5 + I * 2
z_list = [z0]

for i in range(20):
    df_dx, df_dy = df(z0)
    dz = f(z0) / (df_dx + df_dy)
    z = z0 - dz
    z_list.append(z)
    z0 = z

print(z_list)