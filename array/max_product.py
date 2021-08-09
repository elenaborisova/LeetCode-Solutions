def max_product(nums):
    first_num = nums.pop(nums.index(max(nums)))
    second_num = max(nums)

    result = (first_num - 1) * (second_num - 1)
    return result


print(max_product([3, 4, 5, 2]))
print(max_product([1, 5, 4, 5]))
print(max_product([3, 7]))
