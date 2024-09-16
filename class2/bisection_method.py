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
def f(x):
    return x**3 + 4*x - 9
bisection_method(2, 3, 0.01)

# 1-
import numpy as np  # Importa o pacote NumPy como 'np', 
                    # que é uma biblioteca usada para computação científica em Python

def f(x):
    return x**3 - 10*x**2 + 5  # Retorna o resultado da expressão matemática x^3 - 10x^2 + 5 para o valor de entrada 'x'

def meu_metodo(f, a, b, tol):
    if np.sign(f(a)) == np.sign(f(b)):
        raise Exception("Não existe raiz no intervalo [a, b]")  # Levanta uma exceção caso não 
                                                                # exista raiz no intervalo fornecido
    m = (a + b) / 2  # Calcula o ponto médio entre os valores de entrada 'a' e 'b'
    if np.abs(f(m)) < tol:
        return m  # Retorna o ponto médio como aproximação da raiz se a condição anterior for verdadeira
    elif np.sign(f(a)) == np.sign(f(m)):
        return meu_metodo(f, m, b, tol)  # Chama recursivamente a própria função com 'm' e 'b' como novos limites
    else:
        return meu_metodo(f, a, m, tol)  # Chama recursivamente a própria função com 'a' e 'm' como novos limites

a = 0  # Define o limite inferior do intervalo
b = 1  # Define o limite superior do intervalo
tol = 10**(-6)  # Define a tolerância para a aproximação da raiz
raiz_approx = meu_metodo(f, a, b, tol)  # Chama a função 'meu_metodo' e armazena o resultado em 'raiz_approx'
print("raiz_approx:", raiz_approx)  # Imprime a raiz aproximada
