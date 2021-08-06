def create_target_array(nums, index):
    target = []

    for i in range(len(nums)):
        target.insert(index[i], nums[i])

    return target


print(create_target_array([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
print(create_target_array([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
print(create_target_array([1], [0]))
