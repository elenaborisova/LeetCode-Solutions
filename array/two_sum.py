def two_sum(nums, target):
    # Time: O(n^2)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_optimized(nums, target):
    # Time: O(n)
    d = {}

    for i, n in enumerate(nums):
        m = target - n
        if m in d:
            return [d[m], i]
        d[n] = i


# Test cases:
print(two_sum_optimized([2, 7, 11, 15], 9) == [0, 1])
print(two_sum([3, 2, 4], 6) == [1, 2])
print(two_sum([3, 3], 6) == [0, 1])
