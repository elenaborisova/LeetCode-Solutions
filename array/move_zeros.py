def move_zeros(nums):
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == 0:
            nums.append(nums.pop(i))

    return nums


print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([0]))

