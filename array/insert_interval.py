def insert(intervals, new_interval):
    result = []

    for interval in intervals:

        if interval[1] < new_interval[0]:
            result.append(interval)

        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval

        elif interval[1] >= new_interval[0] or interval[0] <= new_interval[1]:
            new_interval[0] = min(interval[0], new_interval[0])
            new_interval[1] = max(new_interval[1], interval[1])

    result.append(new_interval)
    return result


# Test cases:
print(insert(intervals=[[1, 3], [6, 9]], new_interval=[2, 5]) == [[1, 5], [6, 9]])
print(insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], new_interval=[4, 8]) == [[1, 2], [3, 10], [12, 16]])
print(insert(intervals=[], new_interval=[5, 7]) == [[5, 7]])
print(insert(intervals=[[1, 5]], new_interval=[2, 7]) == [[1, 7]])
print(insert(intervals=[[1, 5]], new_interval=[6, 8]) == [[1, 5], [6, 8]])
print(insert(intervals=[[1, 5]], new_interval=[0, 3]) == [[0, 5]])
print(insert(intervals=[[1, 5]], new_interval=[0, 0]) == [[0, 0], [1, 5]])
print(insert(intervals=[[0, 5], [9, 12]], new_interval=[7, 16]) == [[0, 5], [7, 16]])
print(insert(intervals=[[3, 5], [12, 15]], new_interval=[6, 6]) == [[3, 5], [6, 6], [12, 15]])
