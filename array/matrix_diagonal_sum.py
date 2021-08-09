def diagonal_sum(mat):
    first_diagonal_sum = 0
    second_diagonal_sum = 0

    for row in range(len(mat)):
        for col in range(row, len(mat)):
            if row == col:
                first_diagonal_sum += mat[row][col]

    for i in range(len(mat)):
        row = i
        col = len(mat) - 1 - i
        if not row == col:
            second_diagonal_sum += mat[row][col]

    return first_diagonal_sum + second_diagonal_sum


print(diagonal_sum([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]))

print(diagonal_sum([[1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1],
                    [1, 1, 1, 1]]))

print(diagonal_sum([[5]]))
