import math

a = -4
b = 4
e = 0.01

def f(x):
    return 2 * x**3 - x**2 + x - 1

if f(a)*f(b) < 0:
    while(math.fabs(b-a)/2 > e):
        m = (a+b)/2
        if f(m) == 0:
            print("A raiz é: ", m)
            break
        elif f(a) * f(m) < 0:
            b = m
        else:
            a = m
    print("O valor aproximado é: ", m)
else:
    print('Não existe raiz no intervalo')