def pair_sum(a, b):
    return a + b


def pair_sum_sequence(n):
    total_sum = 0

    for i in range(n):
        total_sum += pair_sum(i, i + 1)

    return total_sum


print(pair_sum_sequence(2))

# Time: O(n) calls to pair_sum
# Space: O(1) as the calls do not exist simultaneously on the call stack
