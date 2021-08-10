def maximum_units(box_types, truck_size):
    boxes_count = 0
    max_units = 0

    box_types = sorted(box_types, key=lambda x: x[1], reverse=True)

    for box in box_types:
        box_count = box[0]
        box_units = box[1]

        if boxes_count + box_count <= truck_size:
            boxes_count += box_count
            max_units += box_count * box_units
        else:
            max_units += (truck_size - boxes_count) * box_units
            break

    return max_units


print(maximum_units(box_types=[[1, 3], [2, 2], [3, 1]], truck_size=4))
print(maximum_units([[5, 10], [2, 5], [4, 7], [3, 9]], 10))
