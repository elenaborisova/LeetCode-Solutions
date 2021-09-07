from collections import deque


def shift_grid(grid, k):
    m, n = len(grid), len(grid[0])
    elements = deque([grid[row][col] for row in range(m) for col in range(n)])
    elements.rotate(k)
    elements.reverse()
    rotated_grid = []

    for r in range(m):
        curr_row = []
        for col in range(n):
            curr_row.append(elements.pop())
        rotated_grid.append(curr_row)

    return rotated_grid


print(shift_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))
print(shift_grid([[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]], 4))
print(shift_grid([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9))
