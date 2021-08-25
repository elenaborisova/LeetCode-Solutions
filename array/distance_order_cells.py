def all_cells_dist_order(rows, cols, r_center, c_center):
    curr_pos = [r_center, c_center]
    coordinates = {}

    for row in range(rows):
        for col in range(cols):
            distance = abs(row - curr_pos[0]) + abs(col - curr_pos[1])
            coordinates[row, col] = distance

    sorted_coordinates = dict(sorted(coordinates.items(), key=lambda x: x[1]))
    final_coordinates = [list(key) for key in sorted_coordinates.keys()]

    return final_coordinates


print(all_cells_dist_order(1, 2, 0, 0))
print(all_cells_dist_order(2, 2, 0, 1))
print(all_cells_dist_order(2, 3, 1, 2))
