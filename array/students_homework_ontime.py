def busy_student(start_time, end_time, query_time):
    ontime_students_count = 0

    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            ontime_students_count += 1

    return ontime_students_count


print(busy_student([1, 2, 3], [3, 2, 7], 4))
print(busy_student([4], [4], 4))
print(busy_student([1, 1, 1, 1], [1, 3, 2, 4], 7))
print(busy_student([9, 8, 7, 6, 5, 4, 3, 2, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10], 5))
