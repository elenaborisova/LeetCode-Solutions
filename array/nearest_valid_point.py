import sys


def nearest_valid_point(x, y, points):
    valid_points = [p for p in points if p[0] == x or p[1] == y]
    nearest_point = []
    min_distance = sys.maxsize

    for p in valid_points:
        distance = abs(x - p[0]) + abs(y - p[1])
        if distance < min_distance:
            min_distance = distance
            nearest_point = p

    return points.index(nearest_point) if nearest_point else -1


print(nearest_valid_point(3, 4, [[1, 2], [3, 1], [2, 4], [2, 3], [4, 4]]))
print(nearest_valid_point(3, 4, [[3, 4]]))
print(nearest_valid_point(3, 4, [[2, 3]]))
