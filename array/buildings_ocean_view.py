def get_ocean_view_buildings(heights):
    buildings = []
    prev_max_h = 0

    for i in range(len(heights) - 1, -1, -1):
        h = heights[i]

        if h > prev_max_h:
            buildings.append(i)
            prev_max_h = h

    return buildings[::-1]


# Test cases:
print(get_ocean_view_buildings([4, 2, 3, 1]) == [0, 2, 3])
print(get_ocean_view_buildings([1, 2, 3, 4]) == [3])
print(get_ocean_view_buildings([4, 3, 2, 1]) == [0, 1, 2, 3])
