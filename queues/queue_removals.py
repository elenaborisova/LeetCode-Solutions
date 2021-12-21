from collections import deque


def find_positions(arr, x):
    queue = deque([[d, i] for i, d in enumerate(arr)])
    positions = []

    while queue and len(positions) < x:
        popped = []
        pop_count = x
        while pop_count and queue:
            popped.append(queue.popleft())
            pop_count -= 1

        max_el = max(popped, key=lambda pair: pair[0])
        positions.append(max_el[1] + 1)
        popped.remove(max_el)

        for i in range(len(popped)):
            if popped[i][0] > 0:
                popped[i][0] -= 1

        queue.extend(popped)

    return positions


print(find_positions([1, 2, 2, 3, 4, 5], 5))
print(find_positions([2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4], 4))
