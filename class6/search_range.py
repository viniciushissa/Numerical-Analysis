def f(x):
    return x**3  - 10*x**2 + 5

def procura_intervalo(a, b, delta_x):
    x1 = a
    x2 = a + delta_x
    f1 = f(a)
    f2 = f(x2)

    while f1 * f2 > 0:
        if x1 >= b:
            return None, None
        x1 = x2
        x2 = x1 + delta_x
        f1 = f2
        f2 = f(x2)
    return x1, x2

#valores iniciais
a = 0
b = 1
delta_x = 0.2
na, nb = procura_intervalo(a, b, delta_x)
if na != a and nb != b:
    print(f'Existe raiz no intervalo --> [{na:.3}, {nb:.3}]')
else:
    print('Não existe raiz no intervalo')
