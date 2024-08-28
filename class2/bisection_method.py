import math

def bisection_method(a, b, e):
    iteracoes = 0
    if f(a)*f(b) < 0:
        while(math.fabs(b-a)/2 > e):
            iteracoes += 1
            m = (a+b)/2
            if f(m) == 0:
                print("A raiz é: ", m)
                break
            elif f(a) * f(m) < 0:
                b = m
            else:
                a = m
        print(f'O valor aproximado é: {m}')
        print(f'Número de iterações: {iteracoes}\n')
    else:
        print('Não existe raiz no intervalo\n')

print('1-')
def f(x):
    return x**2 - 5
bisection_method(0, 1, 0.01)

print('2-')
def f(x):
    return x**2 - 5
bisection_method(2.2303, 6, 0.01)

print('3.1-')
def f(x):
    return 2 * x**3 - x**2 + x - 1
bisection_method(-4, 4, 0.01)

print('3.2-')
def f(x):
    return 2 * x**3 - x**2 + x - 1
bisection_method(0, 1, 0.01)

print('4-')
def f(x):
    return x**3 + 4 * x**2 - 10
bisection_method(1, 2, 10**-5)

# print('5-')
# def bisection_method(a, b, e):
#     iteracoes = 0
#     if f(a) * f(b) < 0:
#         n = math.ceil(math.log2((b - a) / e))
#         for _ in range(n):
#             iteracoes += 1
#             m = (a + b) / 2
#             if f(m) == 0:
#                 print("A raiz é: ", m)
#                 break
#             elif f(a) * f(m) < 0:
#                 b = m
#             else:
#                 a = m
#         print(f'O valor aproximado é: {m}')
#         print(f'Número de iterações: {iteracoes}\n')
#     else:
#         print('Não existe raiz no intervalo\n')