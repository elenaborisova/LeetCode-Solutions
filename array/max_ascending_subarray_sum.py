def max_ascending_sum(nums):
    max_sum = 0
    curr_sum = 0
    prev_num = 0

    for i in range(len(nums)):
        if nums[i] > prev_num:
            curr_sum += nums[i]
        else:
            max_sum = max(max_sum, curr_sum)
            curr_sum = nums[i]

        prev_num = nums[i]

    return max(max_sum, curr_sum)


print(max_ascending_sum([10, 20, 30, 5, 10, 50]))
print(max_ascending_sum([10, 20, 30, 40, 50]))
print(max_ascending_sum([12, 17, 15, 13, 10, 11, 12]))
print(max_ascending_sum([100, 10, 1]))