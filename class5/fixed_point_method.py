import numpy as np 
import matplotlib.pyplot as plt
import os 

def f(x):
    return np.exp(-x/4)*(2-x)-1

def g(x):
    return 2 - np.exp(x/4)

def ponto_fixo_iterativo(x0, tol, max_iter):
    x = x0
    for i in range(max_iter):
        x_new = g(x)
        if np.abs(x_new - x) < tol:
            print(f'Convergência alcançada após {i+1} iterações.')
            return x_new
        x = x_new
    print('Numero maximo de iterações alcançado')
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

x0 = 0.8
tol = 1e-3
max_iter = 500
os.system('cls')
raiz = ponto_fixo_iterativo(x0, tol, max_iter)
print(f'A raiz aproximada é: {raiz:.8}')
plot_grafico(0, raiz+1)