import math

a = 0
b = 6
e = 0.01

def f(x):
    return x**2 - 5

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