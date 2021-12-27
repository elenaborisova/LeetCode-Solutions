from collections import Counter


def number_of_ways(arr, k):
    # Brute Force; Time: O(n^2)
    pairs_count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                pairs_count += 1

    return pairs_count


def number_of_ways_optimized(arr, k):
    # Time: O(n)
    d = {}
    count = 0

    for i, n in enumerate(arr):
        m = k - n
        if m in d:
            count += d[m]

        if n not in d:
            d[n] = 0
        d[n] += 1

    return count


def pair_sums_optimized2(arr, k):
    a_counter = Counter(arr)
    counter = 0

    for ar in arr:
        if k - ar in a_counter and a_counter[(k - ar)] >= 1:
            if k - ar == ar:
                counter += a_counter[k - ar] - 1
            else:
                counter += a_counter[k - ar]

            a_counter[ar] = a_counter[ar] - 1

    return counter


# Test cases:
print(number_of_ways([1, 2, 3, 4, 3], 6) == 2)
print(number_of_ways([1, 5, 3, 3, 3], 6) == 4)
print(number_of_ways([1, 1, 1, 1, 1, 1], 2) == 15)
print(number_of_ways([100, 99, 1, 51, 49, 49], 100) == 3)
