import math
import numpy as np
import matplotlib.pyplot as plt

a = -2
b = 2
e = 0.01

def f(x):
    return (np.sin(50/(1 + x**2)) + 1 - x**2)

xp = np.linspace(a, b, 100)
yp = f(xp)

plt.plot(xp, yp, color='blue')
plt.title('função sin(50/(1 + x**2)) + 1 - x**2 [-2,2]')
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.grid()

#plt.grid(axis='y')
plt.show()