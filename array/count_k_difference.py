from collections import defaultdict


def count_k_difference(nums, k):
    pairs_count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                pairs_count += 1

    return pairs_count


print(count_k_difference(nums=[1, 2, 2, 1], k=1))
print(count_k_difference(nums=[1, 3], k=3))
print(count_k_difference(nums=[3, 2, 1, 5, 4], k=2))
