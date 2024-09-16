import numpy as np

def resolver_triangular_superior(A, b):
    n = len(b)
    x = np.zeros_like(b, dtype=np.float64)

    for i in range(n-1, -1, -1):
        if A[i, i] == 0:
            raise ValueError("Matriz singular, não é possível resolver")
        
        x[i] = b[i] / A[i, i]
        for j in range(i+1, n):
            x[i] -= A[i, j] * x[j] / A[i, i]

    return x

A = np.array([[2, -1, 3],
              [0, 1, -2],
              [0, 0, 5]], dtype=np.float64)

b = np.array([5, 3, 10], dtype=np.float64)

solucao = resolver_triangular_superior(A, b)
print("Solução do sistema:", solucao)