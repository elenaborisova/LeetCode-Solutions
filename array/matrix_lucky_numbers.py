def lucky_numbers(matrix):
    lucky_nums = []

    for i in range(len(matrix)):
        min_num = min(matrix[i])
        min_num_idx = matrix[i].index(min_num)
        same_column = []
        for j in range(len(matrix)):
            same_column.append(matrix[j][min_num_idx])

        if min_num == max(same_column):
            lucky_nums.append(min_num)

    return lucky_nums


print(lucky_numbers([[3, 7, 8], [9, 11, 13], [15, 16, 17]]))
print(lucky_numbers([[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]))
print(lucky_numbers([[7, 8], [1, 2]]))
