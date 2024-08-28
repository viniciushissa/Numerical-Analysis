from math import log, ceil  # Importa as funções 'log' e 'ceil' da biblioteca math

def f(x):
    return x**2 - 8  # Define a função f(x) = x^2 - 8

def bissecao(f, a, b, e):
    fa = f(a)  # Calcula o valor de f(a)
    if fa == 0.0:
        return a  # Se f(a) é 0, o próprio 'a' é a raiz, então retorna 'a'
    
    fb = f(b)  # Calcula o valor de f(b)
    if fb == 0.0:
        return b  # Se f(b) é 0, 'b' é a raiz, então retorna 'b'
    
    if fa * fb < 0.0: # Se f(a) e f(b) têm sinais opostos, existe uma raiz no intervalo [a, b]
        n = ceil(log(abs(b-a)/e) / log(2.0))  # Calcula o número máximo de iterações necessárias, com base na precisão 'e'
        
        for i in range(n):
            m = 0.5 * (a + b)  # Calcula o ponto médio do intervalo
            fm = f(m)  # Calcula o valor de f(m)
            
            if fm == 0.0:
                return m  # Se f(m) é 0, 'm' é a raiz exata, então retorna 'm'
            
            if fb * fm < 0.0:
                # Se f(m) e f(b) têm sinais opostos, a raiz está no intervalo [m, b]
                a = m  # Atualiza 'a' para 'm'
                fa = fm  # Atualiza f(a) para f(m)
            else:
                # Caso contrário, a raiz está no intervalo [a, m]
                b = m  # Atualiza 'b' para 'm'
                fb = fm  # Atualiza f(b) para f(m)
        
        return (a + b) / 2.0  # Retorna a aproximação da raiz após as iterações
    else:
        print('Não existe raiz no intervalo')  # Se f(a) e f(b) têm o mesmo sinal, não há raiz no intervalo [a, b]
        return None  # Retorna None indicando que não foi encontrada uma raiz