# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.


def zero_matrix(matrix):
    zero_rows = set()
    zero_columns = set()
    n = len(matrix)

    for i in range(n):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_columns.add(j)

    for i in range(n):
        for j in range(len(matrix[i])):
            if i in zero_rows or j in zero_columns:
                matrix[i][j] = 0

    return matrix


print(zero_matrix([[1, 2, 0],
                  [4, 0, 1],
                  [4, 2, 1]]))

