def find_min_idx(i, count, arr, min_element):
    min_idx = 0

    while i <= count and i < len(arr):
        if arr[i] < min_element:
            min_element = arr[i]
            min_idx = i
        i += 1

    return min_idx


def find_min_array(arr, k):
    min_element = 1_000_000
    i = 0
    count = k

    while k:
        min_idx = find_min_idx(i, count, arr, min_element)

        while k and min_idx:
            arr[min_idx], arr[min_idx - 1] = arr[min_idx - 1], arr[min_idx]
            min_idx -= 1
            k -= 1

        i = min_idx + 1
        min_element = 1_000_000

    return arr


# Test cases:
print(find_min_array([5, 3, 1], 2) == [1, 5, 3])
print(find_min_array([8, 9, 11, 2, 1], 3) == [2, 8, 9, 11, 1])
print(find_min_array([5, 6, 1, 2, 6, 7, 8, 9], 3) == [1, 5, 2, 6, 6, 7, 8, 9])
print(find_min_array([8, 9, 11, 2, 1], 5) == [1, 8, 9, 2, 11])
print(find_min_array([8, 9, 11, 2, 1], 6) == [1, 8, 2, 9, 11])
print(find_min_array([5, 6, 1, 2, 6, 7, 8, 9], 100) == [1, 2, 5, 6, 6, 7, 8, 9])
print(find_min_array([5, 3, 1], 0) == [5, 3, 1])
