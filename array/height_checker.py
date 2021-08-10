def height_checker(heights):
    expected = sorted(heights)
    indices_mismatch = 0

    for i in range(len(heights)):
        if not heights[i] == expected[i]:
            indices_mismatch += 1

    return indices_mismatch


print(height_checker([1, 1, 4, 2, 1, 3]))
print(height_checker([5, 1, 2, 3, 4]))
print(height_checker([1, 2, 3, 4, 5]))
