import time


def max_subarray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    size = len(nums)
    i = 1

    while i < size:
        if curr_sum + nums[i] > nums[i]:
            curr_sum += nums[i]
        else:
            curr_sum = nums[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        i += 1

    return max_sum


start_time = time.time()
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(time.time() - start_time)
