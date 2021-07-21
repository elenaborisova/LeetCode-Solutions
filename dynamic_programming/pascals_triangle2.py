def get_row(row_i):
    prev_row = []
    curr_row = []

    for row in range(row_i + 1):
        for col in range(row + 1):
            if col == 0 or col == row:
                curr_row.append(1)
            else:
                curr_row.append(prev_row[col-1] + prev_row[col])

        prev_row = curr_row
        curr_row = []

    return prev_row


print(get_row(4))
