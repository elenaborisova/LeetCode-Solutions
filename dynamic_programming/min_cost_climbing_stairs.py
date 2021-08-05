def min_cost_climbing_stairs(cost):
    n = len(cost)
    last = cost[1]
    second_to_last = cost[0]

    for i in range(2, n):
        current = cost[i] + min(last, second_to_last)
        second_to_last = last
        last = current

    return min(last, second_to_last)


print(min_cost_climbing_stairs([10, 15, 20]))
print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
print(min_cost_climbing_stairs([0, 1, 2, 2]))