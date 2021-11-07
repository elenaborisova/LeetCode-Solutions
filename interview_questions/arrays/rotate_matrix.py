# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?


def transpose_matrix(matrix):
    transposed = [[None for _ in range(len(matrix))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposed[j][i] = matrix[i][j]

    return transposed


def rotate_matrix_by_90degrees(matrix):
    # time: O(n^2)
    transposed = transpose_matrix(matrix)
    rotated = []

    for row in transposed:
        rotated.append(row[::-1])

    return rotated


# Method 2
def rotate_matrix2(matrix):
    # time: O(n^2)
    if len(matrix) == 0 or not len(matrix) == len(matrix[0]):
        return False

    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top

    return matrix


print(rotate_matrix_by_90degrees([[1, 2, 3],
                                  [4, 5, 6],
                                  [7, 8, 9]]))

print(rotate_matrix2([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]))
