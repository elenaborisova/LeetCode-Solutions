def most_visited(n, rounds):
    sectors_visits = {x: 0 for x in range(1, n + 1)}
    prev_end = 0

    for i in range(1, len(rounds)):
        if i == 1:
            start = rounds[i - 1]
        else:
            start = prev_end + 1

        end = rounds[i]
        prev_end = end

        if start > end:
            for j in range(start, n + 1):
                sectors_visits[j] += 1
            for j in range(1, end + 1):
                sectors_visits[j] += 1
        else:
            for j in range(start, end + 1):
                sectors_visits[j] += 1

    most_visits = max(sectors_visits.values())
    most_visited_sectors = sorted([sector for sector, visits in sectors_visits.items() if visits == most_visits])

    return most_visited_sectors


print(most_visited(n=4, rounds=[1, 3, 1, 2]))
print(most_visited(n=2, rounds=[2, 1, 2, 1, 2, 1, 2, 1, 2]))
print(most_visited(n=7, rounds=[1, 3, 5, 7]))
