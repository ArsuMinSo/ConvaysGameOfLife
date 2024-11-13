def matMul(lstMatA, lstMatB):
    # Check if matrix multiplication is possible
    if len(lstMatA[0]) != len(lstMatB):
        raise ValueError("Cannot multiply matrices with incompatible dimensions")
    
    # Initialize the result matrix with the appropriate dimensions
    result = [[0] * len(lstMatB[0]) for _ in range(len(lstMatA))]
    
    # Perform matrix multiplication
    for i in range(len(lstMatA)):  # Iterate over rows of matrix_a
        for j in range(len(lstMatB[0])):  # Iterate over columns of matrix_b
            for k in range(len(lstMatB)):  # Iterate over rows of matrix_b
                result[i][j] += lstMatA[i][k] * lstMatB[k][j]
    
    return result

def rotate_matrix(matrix):
    # Step 1: Transpose the matrix (rows become columns)
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):  # Only traverse the upper triangle (without diagonal)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
    
    return matrix
