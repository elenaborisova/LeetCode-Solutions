def set_zeroes(matrix):
    is_col = False

    for row in range(len(matrix)):
        if matrix[row][0] == 0:
            is_col = True

        for col in range(1, len(matrix[row])):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                matrix[row][0] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[row])):
            if matrix[row][0] == 0 or matrix[0][col] == 0:
                matrix[row][col] = 0

    if matrix[0][0] == 0:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0

    if is_col:
        for row in range(len(matrix)):
            matrix[row][0] = 0

    return matrix


# Test cases:
print(set_zeroes([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(set_zeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]))
print(set_zeroes([[0, 1]]))
