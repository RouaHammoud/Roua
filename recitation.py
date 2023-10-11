import sympy as sp

X= sp.symbols('x')

def f(x):
    return sp.cos(sp.exp(x))

df= sp.diff(f(X))
 
print(df)

print(df.subs(X, 2).evalf())
intg= sp.integrate(f(X))
print(intg)
