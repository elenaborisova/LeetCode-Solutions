def sum_of_unique(nums):
    unique_sum = 0

    for num in nums:
        if nums.count(num) == 1:
            unique_sum += num

    return unique_sum


print(sum_of_unique([1, 2, 3, 2]))
print(sum_of_unique([1, 1, 1, 1, 1]))
print(sum_of_unique([1, 2, 3, 4, 5]))
