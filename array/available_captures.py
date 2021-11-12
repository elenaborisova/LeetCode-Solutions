def num_rook_captures(board):
    rook_pos = [[row, col] for col in range(8) for row in range(8) if board[row][col] == 'R'][0]
    directions = {
        'up': (-1, 0),
        'down': (1, 0),
        'right': (0, 1),
        'left': (0, -1),
    }
    captures = 0

    for dir in directions:
        new_row, new_col = rook_pos[0], rook_pos[1]
        while True:
            new_row += directions[dir][0]
            new_col += directions[dir][1]
            if not 0 <= new_row < 8 or not 0 <= new_col < 8:
                break

            if board[new_row][new_col] == 'p':
                captures += 1
                break
            elif board[new_row][new_col] == 'B':
                break

    return captures


print(num_rook_captures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))

print(num_rook_captures([[".", ".", ".", ".", ".", ".", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "B", "R", "B", "p", ".", "."],
                         [".", "p", "p", "B", "p", "p", ".", "."], [".", "p", "p", "p", "p", "p", ".", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))

print(num_rook_captures([[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
                         [".", ".", ".", "p", ".", ".", ".", "."], ["p", "p", ".", "R", ".", "p", "B", "."],
                         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "B", ".", ".", ".", "."],
                         [".", ".", ".", "p", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]))