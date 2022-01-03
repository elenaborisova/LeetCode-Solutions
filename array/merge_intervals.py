def merge(intervals):
    intervals.sort()
    res = []
    current = intervals[0].copy()

    for interval in intervals[1:]:
        if current[1] < interval[0]:
            res.append(current)
            current = interval
        elif current[0] > interval[1]:
            res.append(current)
            current = interval
        elif current[0] <= interval[1] or current[1] >= interval[0]:
            current[0] = min(current[0], interval[0])
            current[1] = max(current[1], interval[1])
    res.append(current)

    return res


def merge2(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:

        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


# Test cases:
print(merge2([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]])
print(merge2([[1, 4], [4, 5]]) == [[1, 5]])
print(merge2([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]) == [[1, 10]])
