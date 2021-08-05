def build_array(nums):
    permutated_array = []

    for i in range(len(nums)):
        permutated_array.append(nums[nums[i]])

    return permutated_array


print(build_array([0, 2, 1, 5, 3, 4]))
print(build_array([5, 0, 1, 2, 3, 4]))
