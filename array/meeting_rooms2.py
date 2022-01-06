def min_meeting_rooms(intervals):
    start = sorted([interval[0] for interval in intervals])
    end = sorted([interval[1] for interval in intervals])

    res, count = 0, 0
    s, e = 0, 0
    while s < len(start):
        if start[s] < end[e]:
            count += 1
            s += 1
        else:
            count -= 1
            e += 1
        res = max(res, count)

    return res


# Test cases:
print(min_meeting_rooms([(0, 30), (5, 10), (15, 20)]) == 2)
print(min_meeting_rooms([(5, 8), (9, 15)]) == 1)
print(min_meeting_rooms([(5, 8)]) == 1)
print(min_meeting_rooms([[1, 2], [2, 3], [3, 4], [1, 3]]) == 2)
print(min_meeting_rooms([[1, 2], [1, 2], [1, 2]]) == 3)
print(min_meeting_rooms([[1, 2], [2, 3]]) == 1)
