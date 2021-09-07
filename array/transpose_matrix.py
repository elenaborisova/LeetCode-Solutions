def transpose_matrix(matrix):
    m, n = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(m)] for _ in range(n)]

    for row in range(m):
        for col in range(n):
            el = matrix[row][col]
            transposed[col][row] = el

    return transposed


print(transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(transpose_matrix([[1, 2, 3], [4, 5, 6]]))
