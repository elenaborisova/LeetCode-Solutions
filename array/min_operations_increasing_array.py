def min_operations(nums):
    operations_count = 0

    if not nums or len(nums) == 1:
        return 0

    i = 0
    while i < len(nums) - 1:
        if nums[i + 1] <= nums[i]:
            diff = nums[i] - nums[i + 1]
            nums[i + 1] += diff + 1
            operations_count += diff + 1
        else:
            i += 1

    return operations_count


print(min_operations([1, 5, 2, 4, 1]))
print(min_operations([1, 1, 1]))
print(min_operations([8]))
print(min_operations([10, 2, 5]))
print(min_operations([3, 5]))
print(min_operations([7, 6, 1, 9, 9, 10]))
