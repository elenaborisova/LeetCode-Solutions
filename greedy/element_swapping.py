import heapq


def find_min_array(arr, k):
    h = []

    i = 0
    while i <= k and i < len(arr):
        heapq.heappush(h, arr[i])
        i += 1

    while k and h:
        min_el = heapq.heappop(h)

        # TODO: handle duplicate values
        idx = arr.index(min_el)
        while idx and k:
            arr[idx], arr[idx - 1] = arr[idx - 1], arr[idx]
            idx -= 1
            k -= 1

    return arr


print(find_min_array([5, 3, 1], 2) == [1, 5, 3])
print(find_min_array([8, 9, 11, 2, 1], 3) == [2, 8, 9, 11, 1])
print(find_min_array([5, 6, 1, 2, 6, 7, 8, 9], 3) == [1, 5, 2, 6, 6, 7, 8, 9])
print(find_min_array([8, 9, 11, 2, 1], 5) == [1, 8, 9, 2, 11])
print(find_min_array([8, 9, 11, 2, 1], 6) == [1, 8, 2, 9, 11])
print(find_min_array([5, 6, 1, 2, 6, 7, 8, 9], 100) == [1, 2, 5, 6, 6, 7, 8, 9])
print(find_min_array([5, 3, 1], 0) == [5, 3, 1])
