def erase_overlap_intervals(intervals):
    # sorting by end
    intervals.sort(key=lambda x: x[1])
    erase_count = 0
    current = intervals[0]

    for interval in intervals[1:]:
        if current[1] > interval[0]:
            erase_count += 1
        else:
            current = interval

    return erase_count


def erase_overlap_intervals2(intervals):
    # sorting by start
    intervals.sort()
    erase_count = 0
    current = intervals[0][1]

    for interval in intervals[1:]:
        if current > interval[0]:
            erase_count += 1
            current = min(current, interval[1])  # remove/skip the one with bigger end value
        else:
            current = interval[1]

    return erase_count


# Test cases:
print(erase_overlap_intervals2([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1)
print(erase_overlap_intervals2([[1, 2], [1, 2], [1, 2]]) == 2)
print(erase_overlap_intervals2([[1, 2], [2, 3]]) == 0)
print(erase_overlap_intervals2(
    [[-52, 31], [-73, -26], [82, 97], [-65, -11], [-62, -49], [95, 99], [58, 95], [-31, 49], [66, 98], [-63, 2],
     [30, 47], [-40, -26]]) == 7)
