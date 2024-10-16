import numpy as np

def gauss_elimination(A, b):
    n = len(b)
    
    augmented_matrix = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        
        if i != max_row:
            augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        
        for j in range(i+1, n):
            factor = augmented_matrix[j, i] / augmented_matrix[i, i]
            augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (augmented_matrix[i, -1] - np.dot(augmented_matrix[i, i+1:n], x[i+1:n])) / augmented_matrix[i, i]
    
    return x, augmented_matrix

A = np.array([[1, 2, 1], 
              [2, 5, -1],
              [3, -2, -1]], dtype=float)
b = np.array([3, -4, 5], dtype=float)

print(f'Matriz A=\n{A} \n b={b}\n')

solucao, augmented_matrix = gauss_elimination(A, b)

print(f'Matriz após Gauss:\n{augmented_matrix}\n')
print("Solução do sistema: b=", solucao)
