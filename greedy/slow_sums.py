from collections import deque
import heapq


def get_total_time(arr):
    # using queue
    arr = deque(sorted(arr, reverse=True))  # n log n
    total_penalty = 0

    while len(arr) > 1:
        current_sum = arr.popleft() + arr.popleft()
        total_penalty += current_sum
        arr.appendleft(current_sum)

    return total_penalty


def get_total_time2(arr):
    # using max heap
    h = [el * -1 for el in arr]
    heapq.heapify(h)  # n log n
    total_penalty = 0

    while len(h) > 1:
        current_sum = heapq.heappop(h) + heapq.heappop(h)
        total_penalty += current_sum * -1
        heapq.heappush(h, current_sum)

    return total_penalty


print(get_total_time2([2, 3, 9, 8, 4]) == 88)
print(get_total_time2([4, 2, 1, 3]) == 26)
