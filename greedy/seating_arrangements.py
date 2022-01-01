from itertools import permutations


def min_overall_awkwardness(arr):
    perms = list(permutations(arr, len(arr)))
    min_awkwardness = 10000

    for p in perms:
        awkwardness = 0
        for i in range(len(p)):
            awkwardness = max(awkwardness, abs(p[i] - p[i - 1]))

        min_awkwardness = min(min_awkwardness, awkwardness)

    return min_awkwardness


print(min_overall_awkwardness([5, 10, 6, 8]) == 4)
print(min_overall_awkwardness([1, 2, 5, 3, 7]) == 4)
