import collections


def min_operations(arr):
    target = ''.join([str(num) for num in sorted(arr)])
    curr = ''.join([str(num) for num in arr])
    queue = collections.deque([(0, curr)])
    visited = set([curr])

    while queue:
        level, curr = queue.popleft()

        if curr == target:
            return level

        for i in range(len(curr)):
            for j in range(i, len(curr)):
                # Reverse elements between i and j (inclusive)
                permutation = curr[:i] + curr[i:j + 1][::-1] + curr[j + 1:]

                if permutation not in visited:
                    visited.add(permutation)
                    queue.append((level + 1, permutation))


# Test cases:
print(min_operations([1, 2, 5, 4, 3]) == 1)
print(min_operations([3, 1, 2]) == 2)
