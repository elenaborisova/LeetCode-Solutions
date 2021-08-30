def min_start_value(nums):
    start_value = 1
    curr_sum = start_value

    for num in nums:
        curr_sum += num
        if curr_sum < 1:
            start_value += 1 - curr_sum
            curr_sum += 1 - curr_sum

    return start_value


print(min_start_value([-3, 2, -3, 4, 2]))
print(min_start_value([1, 2]))
print(min_start_value([1, -2, -3]))
