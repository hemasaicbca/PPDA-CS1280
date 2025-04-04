import numpy as np

# Generate two 3x3 matrices with random integers between 1 and 10
matrix_a = np.random.randint(1, 11, (3, 3))
matrix_b = np.random.randint(1, 11, (3, 3))

# Perform matrix subtraction
subtraction_result = matrix_a - matrix_b

# Perform element-wise division (handling division by zero)
division_result = np.divide(matrix_a, matrix_b, out=np.zeros_like(matrix_a, dtype=float), where=matrix_b != 0)

# Display the results
print("Matrix A:\n", matrix_a)
print("\nMatrix B:\n", matrix_b)
print("\nSubtraction (A - B):\n", subtraction_result)
print("\nElement-wise Division (A ÷ B):\n", division_result)
