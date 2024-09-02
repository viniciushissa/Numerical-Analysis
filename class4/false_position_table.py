import math

def f(x):
    return x**4/10 - 2*x**2 - x - 3*math.sin(x) + 5

tol = 0.0001
a = 0.0
b = 2.0

def falsa_posicao(a, b, fa, fb):
    return a - fa * (b - a) / (fb - fa)

m = falsa_posicao(a, b, f(a), f(b))

print("\nMétodo da Falsa Posição: \n")
while abs(f(m)) > tol:
    print(f"a={a:.5f} b={b:.5f} m={m:.5f}, f(a)={f(a):.5f} f(m)={f(m):.5f} f(b)={f(b):.5f}, (b-a)={b - a:.5f}")

    if f(a) * f(m) < 0:
        b = m
    elif f(b) * f(m) < 0:
        a = m
    else:
        break

    m = falsa_posicao(a, b, f(a), f(b))

print(f"\nFinalmente raiz = {m:.5f}\n")

m = a + (b - a) / 2

print("\nMétodo de Bissecção: \n")
while abs(f(m)) > tol:
    print(f"a={a:.5f} b={b:.5f} m={m:.5f}, f(a)={f(a):.5f} f(m)={f(m):.5f} f(b)={f(b):.5f}, (b-a)={b - a:.5f}")

    if f(a) * f(m) < 0:
        b = m
    elif f(b) * f(m) < 0:
        a = m
    else:
        break

    m = a + (b - a) / 2

print(f"\nFinalmente raiz = {m:.5f}\n")