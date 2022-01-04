def above_average_subarrays(a):
    subarrays = []
    total_sum = sum(a)
    n = len(a)
    l, r = 0, 0

    while l < n:
        subarray = 0
        count = 0

        while r < n:
            subarray += a[r]
            count += 1
            subarray_avg = subarray / count
            rem_avg = (total_sum - subarray) / (n - count) if count != n else 0

            if subarray_avg > rem_avg:
                subarrays.append([l + 1, r + 1])

            r += 1

        l += 1
        r = l

    return subarrays


# Test cases:
print(above_average_subarrays([3, 4, 2]) == [[1, 2], [1, 3], [2, 2]])
print(above_average_subarrays([2]) == [[1, 1]])
print(above_average_subarrays([2, 2, 2, 2]) == [[1, 4]])
print(above_average_subarrays([2, 2, 2, 1]) == [[1, 1], [1, 2], [1, 3], [1, 4], [2, 2], [2, 3], [3, 3]])
print(above_average_subarrays([3, 4, 2, 5, 6]) == [[1, 5], [2, 5], [3, 5], [4, 4], [4, 5], [5, 5]])
print(
    above_average_subarrays([1, 4, 2, 10, 20, 30, 50, 60, 5, 1000000]) == [[1, 10], [2, 10], [3, 10], [4, 10], [5, 10],
                                                                           [6, 10], [7, 10], [8, 10], [9, 10],
                                                                           [10, 10]])
