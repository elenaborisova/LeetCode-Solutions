def running_sum(nums):
    new_nums = []

    for i in range(len(nums)):
        num = sum(nums[:i + 1])
        new_nums.append(num)

    return new_nums


print(running_sum([1, 2, 3, 4]))
print(running_sum([1, 1, 1, 1, 1]))
print(running_sum([3, 1, 2, 10, 1]))
