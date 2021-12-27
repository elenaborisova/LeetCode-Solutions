import heapq


def find_median(arr):
    # Time: O(n log n)

    max_heap = []  # storing smaller half
    min_heap = []  # storing bigger half
    medians = []

    for el in arr:
        if not max_heap or el <= max_heap[0] * -1:
            heapq.heappush(max_heap, el * -1)
        else:
            heapq.heappush(min_heap, el)

        if len(max_heap) - len(min_heap) >= 2:
            heapq.heappush(min_heap, heapq.heappop(max_heap) * -1)
        elif len(min_heap) - len(max_heap) >= 2:
            heapq.heappush(max_heap, heapq.heappop(min_heap) * -1)

        if len(max_heap) > len(min_heap):
            median = max_heap[0] * -1
        elif len(min_heap) > len(max_heap):
            median = min_heap[0]
        else:
            median = (max_heap[0] * -1 + min_heap[0]) // 2

        medians.append(median)

    return medians


# Test cases:
print(find_median([5, 15, 1, 3]) == [5, 10, 5, 4])
print(find_median([5, 5, 15, 1, 3]) == [5, 5, 5, 5, 5])
print(find_median([2, 4, 7, 1, 5, 3]) == [2, 3, 4, 3, 4, 3])
