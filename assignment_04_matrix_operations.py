# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#
def print_matrix(matrix):
    """Utility function to print a matrix in a neat grid format."""
    for row in matrix:
        print(" ".join(f"{val}" for val in row))

def read_matrix(rows, cols, name=""):
    """Helper function to read a matrix from user input row by row."""
    if name:
        print(f"Enter values for Matrix {name}:")
    matrix = []
    for i in range(1, rows + 1):
        row_input = input(f"Enter row {i}: ").strip().split()
        row = [int(x) if x.isdigit() or (x.startswith('-') and x[1:].isdigit()) else float(x) for x in row_input]
        matrix.append(row)
    return matrix

def transpose_matrix(matrix):
    """Computes the transpose of a given matrix (rows become columns)."""
    rows = len(matrix)
    cols = len(matrix[0])
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    return transposed

def add_matrices(matrix_a, matrix_b):
    """Computes element-wise sum of two matrices of the same size."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    """Computes the matrix product A x B."""
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            dot_product = 0
            for k in range(cols_a):
                dot_product += matrix_a[i][k] * matrix_b[k][j]
            row.append(dot_product)
        result.append(row)
    return result

def main():
    print("--- PART A: Transpose Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)
    
    print("\nOriginal Matrix:")
    print_matrix(matrix)
    
    print("\nTransposed Matrix:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed)

if __name__ == "__main__":
    main()


