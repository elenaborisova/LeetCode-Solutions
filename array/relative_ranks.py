def find_relative_ranks(nums):
    medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
    size = len(nums)
    res = [""] * size
    my_map = {}

    for index, digit in enumerate(nums):
        my_map[digit] = index

    nums.sort(reverse=True)

    for i in range(size):
        if i < 3:
            res[my_map[nums[i]]] = medal[i]
        else:
            res[my_map[nums[i]]] = str(i + 1)

    return res


print(find_relative_ranks([5, 4, 3, 2, 1]))
print(find_relative_ranks([10, 3, 8, 9, 4]))
