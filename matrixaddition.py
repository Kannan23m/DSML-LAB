import numpy as np


A = np.array([[2, 4], [6, 8]])
B = np.array([[1, 3], [5, 7]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

addition = A + B
print("\nMatrix Addition:\n", addition)


subtraction = A - B        
print("\nMatrix Subtraction:\n", subtraction)


elementwise_multiplication = A * B
print("\nElement-wise Multiplication:\n", elementwise_multiplication)


elementwise_division = A / B
print("\nElement-wise Division:\n", elementwise_division)


dot_product = np.dot(A, B)
print("\nDot Product (Matrix Multiplication):\n", dot_product)


rank_A = np.linalg.matrix_rank(A)
print("\nRank of Matrix A:", rank_A)

try:
    inverse_A = np.linalg.inv(A)
    print("\nInverse of Matrix A:\n", inverse_A)
except np.linalg.LinAlgError:
    print("\nMatrix A is not invertible.")


product_matrix = np.dot(A, B)
rank_product = np.linalg.matrix_rank(product_matrix)
print("\nProduct Matrix:\n", product_matrix)
print("Rank of Product Matrix:", rank_product)
