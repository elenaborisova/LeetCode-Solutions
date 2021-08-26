def min_abs_difference(arr):
    arr = sorted(arr)
    min_diff = 1000
    pairs = []

    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < min_diff:
            pairs.clear()
            min_diff = abs(arr[i] - arr[i + 1])

        if abs(arr[i] - arr[i + 1]) == min_diff:
            pairs.append([arr[i], arr[i + 1]])

    return pairs


print(min_abs_difference([4, 2, 1, 3]))
print(min_abs_difference([1, 3, 6, 10, 15]))
print(min_abs_difference([3, 8, -10, 23, 19, -4, -14, 27]))
