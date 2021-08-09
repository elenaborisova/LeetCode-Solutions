def count_negatives(grid):
    count = 0

    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] < 0:
                count += 1

    return count


print(count_negatives([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
print(count_negatives([[3, 2], [1, 0]]))
print(count_negatives([[1, -1], [-1, -1]]))
print(count_negatives([[-1]]))
print(count_negatives([[5, 1, 0], [-5, -5, -5]]))
