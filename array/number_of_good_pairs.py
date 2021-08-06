def num_identical_pairs(nums):
    good_pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                good_pairs.append((i, j))

    return len(good_pairs)


print(num_identical_pairs([1, 2, 3, 1, 1, 3]))
print(num_identical_pairs([1, 1, 1, 1]))
print(num_identical_pairs([1, 2, 3]))
