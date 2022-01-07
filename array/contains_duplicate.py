from collections import Counter


def contains_duplicate(nums):
    # Time: O(n log n); Space: O(1)

    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True

    return False


def contains_duplicate2(nums):
    # Time: O(n); Space: O(n)

    counter = {}

    for num in nums:
        if num not in counter:
            counter[num] = 1
        else:
            return True

    return False


# Test cases:
print(contains_duplicate2([1, 2, 3, 1]) == True)
print(contains_duplicate2([1, 2, 3, 4]) == False)
print(contains_duplicate2([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True)