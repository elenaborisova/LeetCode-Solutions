def count_distinct_triangles(arr):
    # Time: n * n log n
    distinct_triangles = []

    for triangle in arr:  # n
        triangle.sort()  # n log n
        if triangle not in distinct_triangles:  # n
            distinct_triangles.append(triangle)

    return len(distinct_triangles)


# Test cases:
print(count_distinct_triangles([[2, 2, 3], [3, 2, 2], [2, 5, 6]]) == 2)
print(count_distinct_triangles([[8, 4, 6], [100, 101, 102], [84, 93, 173]]) == 3)
print(count_distinct_triangles([[5, 8, 9], [5, 9, 8], [9, 5, 8], [9, 8, 5], [8, 9, 5], [8, 5, 9]]) == 1)
print(count_distinct_triangles([[7, 6, 5], [5, 7, 6], [8, 2, 9], [2, 3, 4], [2, 4, 3]]) == 3)
print(count_distinct_triangles([[3, 4, 5], [8, 8, 9], [7, 7, 7]]) == 3)
