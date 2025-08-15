import random

def generate_matrix(rows, cols, min_val=-200, max_val=200):
    """Generate a matrix with random integers of specified size"""
    return [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    """Add two matrices element-wise"""
    # Validate dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same dimensions")
    
    # Properly structured list comprehension
    return [
        [matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))]
        for i in range(len(matrix1))
    ]

# Generate two 10x10 matrices
matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

# Add matrices
matrix_3 = add_matrices(matrix_1, matrix_2)

# Print results with correct formatting
def print_matrix(name, matrix):
    print(f"{name} = [")
    for i, row in enumerate(matrix):
        print("   ", row, "," if i < len(matrix)-1 else "")
    print("]")

print_matrix("matrix_1", matrix_1)
print()
print_matrix("matrix_2", matrix_2)
print()
print_matrix("matrix_3", matrix_3)