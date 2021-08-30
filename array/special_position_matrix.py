def num_special(mat):
    ones_rows = [row for row in range(len(mat)) if mat[row].count(1) == 1]
    ones_positions = [[row, col] for row in range(len(mat)) for col in range(len(mat[0])) if mat[row][col] == 1]
    ones_cols = [pos[1] for pos in ones_positions]
    ones_cols = [col for col in ones_cols if ones_cols.count(col) == 1]

    #TODO


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
