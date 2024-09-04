import numpy as np 
import matplotlib.pyplot as plt
import os 

def ponto_fixo_iterativo(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if np.abs(x_new - x) < tol:
            print(f'Convergência alcançada após {i+1} iterações.')
            return x_new
        x = x_new
    print('Número máximo de iterações alcançado')
    return x

def plot_grafico(a, b):
    xp = np.linspace(a, b, 100)
    yp = f(xp)
    plt.plot(xp, yp, color='blue')
    plt.axhline(0, color='r')
    plt.axvline(raiz, color='r')
    plt.axis([a, b, f(a)-5, f(b)+5])
    plt.title(r"raiz = {:.4}".format(raiz))
    plt.xlabel('eixo x')
    plt.ylabel('eixo y')
    plt.grid()
    plt.show()

def f(x):
    return np.exp(x) - 4*x

def g(x):
    return np.exp(x)/4 # g(x) < 1

x0 = 1 # valor iniciar
tol = 1e-3 # tolerância para parada
max_iter = 500 
raiz = ponto_fixo_iterativo(x0, tol, max_iter)
print(f'A raiz aproximada é: {raiz:.8}')
plot_grafico(0, 1)

def g(x):
    return 4 * x**2 / np.exp(x) # g(x) > 1

x0 = 3
tol = 1e-3
max_iter = 500
raiz = ponto_fixo_iterativo(x0, tol, max_iter)
print(f'A raiz aproximada é: {raiz:.8}')
plot_grafico(2, 3)