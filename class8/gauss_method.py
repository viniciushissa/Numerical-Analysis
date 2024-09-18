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
    
    return x

A = np.array([[0.8, -0.2, -0.2, -0.3], 
              [-0.2, 0.9, -0.2, -0.3], 
              [-0.3, -0.3, 0.8, -0.2],
              [-0.2, -0.2, -0.4, 0.8]], dtype=float)
b = np.array([0.5, 0.4, 0.3, 0], dtype=float)

solucao = gauss_elimination(A, b)
print("Solução do sistema:", solucao)
