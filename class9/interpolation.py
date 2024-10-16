def gauss_elimination(A, b):
    n = len(b)
    
    # Aplicando eliminação de Gauss
    for i in range(n):
        # Pivotamento
        if A[i][i] == 0.0:
            raise ValueError("Divisão por zero detectada!")
        
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            
            # Elimina as entradas abaixo do pivô
            for k in range(n):
                A[j][k] = A[j][k] - ratio * A[i][k]
            b[j] = b[j] - ratio * b[i]
    
    # Resolvendo o sistema triangular superior
    x = [0 for i in range(n)]
    x[n-1] = b[n-1] / A[n-1][n-1]
    
    for i in range(n-2, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] = x[i] - A[i][j] * x[j]
        x[i] = x[i] / A[i][i]
    
    return x

def interpolacao_polinomial(x, fx):
    n = len(x)
    
    # Monta a matriz de Vandermonde manualmente
    A = [[x[i]**(n-j-1) for j in range(n)] for i in range(n)]
    
    # Resolve o sistema linear Ax = fx
    coeficientes = gauss_elimination(A, fx[:])  # Faz uma cópia de fx
    
    # Monta o polinômio como string
    polinomio = ""
    for i, coef in enumerate(coeficientes):
        if coef != 0:
            if n-i-1 == 0:
                polinomio += f"{coef:.3f}"
            else:
                polinomio += f"{coef:.3f}*x^{n-i-1} + "

    return polinomio

# Exemplo de uso:
x = [0.1, 0.6, 0.8]
fx = [1.221, 3.320, 4.953]

polinomio = interpolacao_polinomial(x, fx)
print("Polinômio interpolador:")
print(polinomio)