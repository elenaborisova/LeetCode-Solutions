def smallest_range(nums, k):
    difference = max(nums) - min(nums)
    if 2 * k >= difference:
        return 0
    else:
        return difference - 2 * k


print(smallest_range([0, 10], 2))
print(smallest_range([1, 3, 6], 3))
print(smallest_range([1], 0))
print(smallest_range([9, 9, 2, 8, 7], 4))
