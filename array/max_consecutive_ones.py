def find_max_consecutive_ones(nums):
    total_count = 0
    curr_count = 0

    for num in nums:
        if num == 1:
            curr_count += 1
        elif num == 0:
            total_count = max(total_count, curr_count)
            curr_count = 0

    return max(total_count, curr_count)


print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))
