import math


def get_billion_users_day(growth_rates):
    # Brute Force
    target = 1_000_000_000

    t = 1
    while True:
        total_users = 0

        for g in growth_rates:
            total_users += g ** t

        if total_users >= target:
            return t

        t += 1


def get_total_rates(growth_rates, t):
    total_users = 0

    for g in growth_rates:
        total_users += g ** t

    return total_users


def get_billion_users_day_optimized(growth_rates):
    target = 1_000_000_000
    high = math.ceil(math.log(target, min(growth_rates)))
    low = math.floor(math.log(target, max(growth_rates)))

    while low < high:
        mid = low + (high - low) // 2
        total_users = get_total_rates(growth_rates, mid)

        if target > total_users:
            low = mid + 1
        else:
            high = mid

    return low


# Test cases
print(get_billion_users_day([1.5]) == 52)
print(get_billion_users_day([1.1, 1.2, 1.3]) == 79)
print(get_billion_users_day([1.01, 1.02]) == 1047)
