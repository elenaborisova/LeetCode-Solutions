def contains_duplicate(nums, k):
    d = {}

    for i, n in enumerate(nums):
        if n in d and i - d[n] <= k:
            return True
        d[n] = i

    return False


# Test cases:
print(contains_duplicate([1, 2, 3, 1], 3) == True)
print(contains_duplicate([1, 0, 1, 1], 1) == True)
print(contains_duplicate([1, 2, 3, 1, 2, 3], 2) == False)
