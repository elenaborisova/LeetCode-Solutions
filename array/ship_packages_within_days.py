def get_days(weights, capacity):
    days = 0
    current_capacity = 0

    for w in weights:
        current_capacity += w
        if current_capacity > capacity:
            days += 1
            current_capacity = w
    days += 1

    return days


def ship_within_days(weights, days):
    min_capacity = max(weights)
    max_capacity = sum(weights)

    while min_capacity < max_capacity:
        mid_capacity = (min_capacity + max_capacity) // 2
        current_days = get_days(weights, mid_capacity)

        if current_days > days:
            min_capacity = mid_capacity + 1
        elif current_days < days:
            max_capacity = mid_capacity - 1
        else:  # if equal
            max_capacity = mid_capacity

    return min_capacity


# Test cases:
print(ship_within_days([3, 2, 2, 4, 1, 4], 3) == 6)
print(ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == 15)
print(ship_within_days([1, 2, 3, 1, 1], 4) == 3)
print(ship_within_days([10, 50, 100, 100, 50, 100, 100, 100], 5) == 160)
