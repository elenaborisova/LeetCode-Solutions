def odd_cells(m, n, indices):
    matrix = [[0 for _ in range(n)] for _ in range(m)]
    odd_nums_count = 0

    for i in indices:
        row = i[0]
        col = i[1]
        for j in range(n):
            matrix[row][j] += 1

        for k in range(m):
            matrix[k][col] += 1

    for row in range(m):
        for col in range(n):
            if matrix[row][col] % 2 == 1:
                odd_nums_count += 1

    return odd_nums_count


print(odd_cells(m=2, n=3, indices=[[0, 1], [1, 1]]))
print(odd_cells(m=2, n=2, indices=[[1, 1], [0, 0]]))
