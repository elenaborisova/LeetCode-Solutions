def k_length_apart(nums, k):
    if 1 in nums:
        last_one_idx = nums.index(1)
    else:
        return True

    for i in range(last_one_idx + 1, len(nums)):
        if nums[i] == 1:
            if i - last_one_idx - 1 < k:
                return False
            last_one_idx = i

    return True

    # ones_indices = [i for i in range(len(nums)) if nums[i] == 1]
    #
    # for i in range(1, len(ones_indices)):
    #     idx = ones_indices[i]
    #     if len(nums[ones_indices[i-1] + 1:idx]) < k:
    #         return False
    #
    # return True


print(k_length_apart([1, 0, 0, 0, 1, 0, 0, 1], 2))
print(k_length_apart([1, 0, 0, 1, 0, 1], 2))
print(k_length_apart([1, 1, 1, 1, 1], 0))
print(k_length_apart([0, 1, 0, 1], 1))
