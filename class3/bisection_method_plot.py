import math
import numpy as np
import matplotlib.pyplot as plt

def plot(a, b, funcao):
    xp = np.linspace(a, b, 100)
    yp = f(xp)

    plt.plot(xp, yp, color='blue')
    plt.title(f'função {funcao}')
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.grid()
    plt.show()

def f(x):
    return x**2 - x - 1
plot(-2, 2, 'x**2 - x - 1')

def f(x):
    return x**3 - 3 * np.sin(x)
plot(-2, 2, 'x**3 - 3 * sin(x)')

def f(x):
    return np.exp(x) - 2
plot(-2, 2, 'exp(x) - 2')

def f(x):
    return np.sin(50/(1 + x**2)) + 1 - x**2
plot(-2, 2, 'sin(50/(1 + x**2)) + 1 - x**2')