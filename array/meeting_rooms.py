def can_attend_meetings(intervals):
    if not intervals:
        return False

    intervals.sort()
    current = intervals[0]

    for interval in intervals[1:]:
        if current[1] > interval[0]:
            return False
        current = interval

    return True


print(can_attend_meetings([(0, 30), (5, 10), (15, 20)]) == False)
print(can_attend_meetings([(5, 8), (9, 15)]) == True)
