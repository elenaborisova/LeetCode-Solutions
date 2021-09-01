def num_special(mat):
    ones_positions = [[row, col] for row in range(len(mat)) for col in range(len(mat[0])) if mat[row][col] == 1]
    cols = [pos[1] for pos in ones_positions]
    special_cols = [col for col in cols if cols.count(col) == 1]
    special_count = 0

    for pos in ones_positions:
        row = pos[0]
        col = pos[1]

        if col in special_cols and mat[row].count(1) == 1:
            special_count += 1

    return special_count


print(num_special([[1, 0, 0],
                   [0, 0, 1],
                   [1, 0, 0]]))

print(num_special([[1, 0, 0],
                   [0, 1, 0],
                   [0, 0, 1]]))

print(num_special([[0, 0, 0, 1],
                   [1, 0, 0, 0],
                   [0, 1, 1, 0],
                   [0, 0, 0, 0]]))

print(num_special([[0, 0, 0, 0, 0],
                   [1, 0, 0, 0, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 1, 0, 0],
                   [0, 0, 0, 1, 1]]))

print(num_special([[0, 0, 1, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 1, 0, 0]]))

print(num_special(
    [[0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 1],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [1, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 1, 1, 0, 0, 0, 0]]))
