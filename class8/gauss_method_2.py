import numpy as np

def gauss_jordan(A, b):
    n = len(b)
    
    augmented_matrix = np.hstack([A, b.reshape(-1, 1)])
    
    for i in range(n):
        max_row = np.argmax(np.abs(augmented_matrix[i:, i])) + i
        
        if i != max_row:
            augmented_matrix[[i, max_row]] = augmented_matrix[[max_row, i]]
        
        augmented_matrix[i] = augmented_matrix[i] / augmented_matrix[i, i]
        
        for j in range(i+1, n):
            factor = augmented_matrix[j, i]
            augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]
    
    for i in range(n-1, -1, -1):
        for j in range(i-1, -1, -1):
            factor = augmented_matrix[j, i]
            augmented_matrix[j] = augmented_matrix[j] - factor * augmented_matrix[i]
    
    x = augmented_matrix[:, -1]
    
    return augmented_matrix, x

A = np.array([[1, -2, 3], 
              [-1, 3, 0], 
              [2, -5, 5]], dtype=float)
b = np.array([9, -4, 17], dtype=float)

augmented_matrix, solucao = gauss_jordan(A, b)

print("Matriz aumentada após Gauss-Jordan:\n", augmented_matrix)
print("Solução do sistema:", solucao)
