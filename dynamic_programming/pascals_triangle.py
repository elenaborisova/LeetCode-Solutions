def get_row(rows_count):
    rows = []
    curr_row = []

    for row in range(rows_count):
        for col in range(row + 1):
            if col == 0 or col == row:
                curr_row.append(1)
            else:
                curr_row.append(rows[-1][col-1] + rows[-1][col])

        rows.append(curr_row)
        curr_row = []

    return rows


print(get_row(4))
