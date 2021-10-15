def is_monotonic(nums):
    return nums == sorted(nums) or nums == sorted(nums)[::-1]


print(is_monotonic([1, 2, 2, 3]))
print(is_monotonic([6, 5, 4, 4]))
print(is_monotonic([1, 3, 2]))
print(is_monotonic([1, 2, 4, 5]))
print(is_monotonic([1, 1, 1]))
