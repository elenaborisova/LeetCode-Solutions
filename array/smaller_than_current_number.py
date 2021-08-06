def smaller_numbers_than_current(nums):
    smaller_nums = []

    for i in range(len(nums)):
        current_smaller = len([x for x in nums if x < nums[i]])
        smaller_nums.append(current_smaller)

    return smaller_nums


print(smaller_numbers_than_current([8, 1, 2, 2, 3]))
print(smaller_numbers_than_current([6, 5, 4, 8]))
print(smaller_numbers_than_current([7, 7, 7, 7]))
