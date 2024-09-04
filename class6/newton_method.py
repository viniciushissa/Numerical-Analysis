import numpy as np
import sympy as sp
from sympy import *

def f(x):
    return x + exp(x) - 2

def newton(p0, max_iter):
    # p0 de forma que f'(p0) != 0
    _iter = 0 
    # valores inicias
    error_x = 1
    epsilon = 10 **(-10)
    x = sp.symbols('x')
    p0_aux = float(p0)
    print('Método de Newton')
    while((error_x > epsilon) and (_iter < max_iter)):
        d = sp.diff(f(x), x)
        vfuncao = f(p0_aux)
        vderivada = d.subs(x, p0_aux)
        p = p0_aux - vfuncao / vderivada
        error_x = abs(p - p0_aux)
        print(f'iteração = {_iter}\nvalor de p = {p}')
        _iter += 1
        p0_aux = p
    return p

max_iter = 100
print(f'Zero aproximado: {newton(0.5, max_iter)}')