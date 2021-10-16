def maximum_difference(nums):
    max_diff = -1

    for i in range(len(nums) - 1):
        diff = max(nums[i + 1:]) - nums[i]
        if diff:
            max_diff = max(max_diff, diff)

    return max_diff


print(maximum_difference([7, 1, 5, 4]))
print(maximum_difference([1, 5, 2, 10]))
print(maximum_difference([9, 4, 3, 2]))
