def is_toeplitz_matrix(matrix):
    groups = {}
    for r, row in enumerate(matrix):
        for c, val in enumerate(row):
            if r - c not in groups:
                groups[r - c] = val
            elif groups[r - c] != val:
                return False
    return True

    # if len(matrix) == 1:
    #     return True
    # else:
    #     for i in range(len(matrix) - 1):
    #         if matrix[i][:-1] != matrix[i + 1][1:]:
    #             return False
    #     return True


print(is_toeplitz_matrix([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]))
print(is_toeplitz_matrix([[1, 2], [2, 2]]))
print(is_toeplitz_matrix([[18], [66]]))
print(is_toeplitz_matrix([[11, 74, 0, 93],
                          [40, 11, 74, 7]]))
