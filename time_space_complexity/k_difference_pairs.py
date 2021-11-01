# Brute Force; Time: O(n ^ 2)
def k_diff_pairs(nums, k):
    pairs = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                pairs.append((nums[i], nums[j]))

    return pairs


# Hashing; Time: O(n)
def k_diff_pairs1(nums, k):
    elements = {}
    pairs = []

    for num in nums:
        elements[num] = True

    for num in nums:
        if elements.get(num + k):
            pairs.append((num, num + k))
        if elements.get(num - k):
            pairs.append((num, num - k))

        elements[num] = False

    return pairs


print(k_diff_pairs1([1, 7, 5, 9, 2, 12, 3], 2))
