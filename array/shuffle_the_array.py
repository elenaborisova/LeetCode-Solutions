def shuffle(nums, n):
    shuffled_array = []

    i = 0
    while len(shuffled_array) < len(nums):
        shuffled_array.append(nums[i])
        shuffled_array.append(nums[i + n])
        i += 1

    return shuffled_array


print(shuffle([2, 5, 1, 3, 4, 7], 3))
print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(shuffle([1, 1, 2, 2], 2))
