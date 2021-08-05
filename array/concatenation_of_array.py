def get_concatenation(nums):
    new_nums = []

    for i in range(2):
        for j in range(len(nums)):
            new_nums.append(nums[j])

    return new_nums


print(get_concatenation([1, 2, 1]))
print(get_concatenation([1, 3, 2, 1]))
