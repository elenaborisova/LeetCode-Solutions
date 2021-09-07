def reshape_matrix(mat, r, c):
    all_elements = [mat[row][col] for row in range(len(mat)) for col in range(len(mat[0]))]
    all_elements.reverse()
    reshaped = []

    try:
        for row in range(r):
            curr_row = []
            for col in range(c):
                curr_row.append(all_elements.pop())
            reshaped.append(curr_row)
        return reshaped if not all_elements else mat
    except IndexError:
        return mat


print(reshape_matrix([[1, 2], [3, 4]], r=1, c=4))
print(reshape_matrix(mat=[[1, 2], [3, 4]], r=2, c=4))
print(reshape_matrix([[1, 2]], 1, 1))
