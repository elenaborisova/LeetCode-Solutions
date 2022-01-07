from collections import Counter
import heapq


def top_k_frequent_heap(nums, k):
    # Time complexity: O(n log k); Space: O(n + k)
    if k == len(nums):
        return nums

    frequency = Counter(nums)
    h = []

    for num in frequency:
        heapq.heappush(h, (frequency[num], num))
        if len(h) > k:
            heapq.heappop(h)

    result = [pair[1] for pair in h]
    return result


def top_k_frequent_heap2(nums, k):
    if k == len(nums):
        return nums

    frequency = Counter(nums)

    return heapq.nlargest(k, frequency.keys(), key=frequency.get)


def top_k_frequent_bucket_sort(nums, k):
    # Time complexity: O(n); Space: O(n)
    if k == len(nums):
        return nums

    counter = Counter(nums)
    frequency = [[] for _ in range(len(nums) + 1)]

    for num, freq in counter.items():
        frequency[freq].append(num)

    result = []

    for i in range(len(frequency) - 1, 0, -1):
        nums = frequency[i]
        for num in nums:  # total of N times (not N times each iteration of the outer loop)
            result.append(num)
            if len(result) == k:
                return result


# Test cases:
print(top_k_frequent_bucket_sort([1, 1, 1, 2, 2, 3], 2))  # return in any order ([1, 2] == [2, 1])
print(top_k_frequent_bucket_sort([1], 1) == [1])
print(top_k_frequent_bucket_sort([-1, -1], 1) == [-1])
