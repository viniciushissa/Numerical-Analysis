import math

def erro_absoluto(x, valor_aproximado):
    return abs(x - valor_aproximado)

def erro_relativo(x, valor_aproximado): 
    erro_temp = erro_absoluto(x, valor_aproximado)
    return erro_temp / abs(valor_aproximado)

def print_valor(v_absoluto, v_relativo):
    print(f'Erro Absoluto : {v_absoluto:.6f}')
    print(f'Erro Relativo : {v_relativo:.6f}\n')
    
pi = 3.141592
e = 2.718282

erro_1_absoluto = erro_absoluto(231.29, 232.04)
erro_1_relativo = erro_relativo(231.29, 232.04)
print_valor(erro_1_absoluto, erro_1_relativo)

erro_2_absoluto = erro_absoluto(0.5682, 0.5701)
erro_2_relativo = erro_relativo(0.5682, 0.5701)
print_valor(erro_2_absoluto, erro_2_relativo)

erro_3_absoluto = erro_absoluto(12.329, 12.331)
erro_3_relativo = erro_relativo(12.329, 12.331)
print_valor(erro_3_absoluto, erro_3_relativo)

print('-----------------------------------')
print('1-\n')
print_valor(erro_absoluto(pi, 22/7), erro_relativo(pi, 22/7))
print_valor(erro_absoluto(pi, 3.1416), erro_relativo(pi, 3.1416))
print_valor(erro_absoluto(e, 2.718), erro_relativo(e, 2.718))
print_valor(erro_absoluto(math.sqrt(2), 1.414), erro_relativo(math.sqrt(2), 1.414))

print('2-\n')
print_valor(erro_absoluto(e**10, 22000), erro_relativo(e**10, 22000))
print_valor(erro_absoluto(10**pi, 1400), erro_relativo(10**pi, 1400))
print_valor(erro_absoluto(math.factorial(8), 39900), erro_relativo(math.factorial(8), 39900))
print_valor(erro_absoluto(math.factorial(9), math.sqrt(18 * pi) * (9 / e)**9), 
            erro_relativo(math.factorial(9), math.sqrt(18 * pi) * (9 / e)**9))