# DP; Time: O(n); Space: O(1)
def max_subarray(nums):
    for i in range(1, len(nums)):
        if nums[i - 1] > 0:
            nums[i] += nums[i - 1]

    return max(nums)


# Time: O(n); Space: O(1)
def max_subarray2(nums):
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(len(nums)):
        if curr_sum + nums[i] > nums[i]:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        # curr_sum = max(nums[i], curr_sum + nums[i])
        # max_sum = max(max_sum, curr_sum)

    return max_sum


# Test cases:
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6)
print(max_subarray([1]) == 1)
print(max_subarray([5, 4, -1, 7, 8]) == 23)
