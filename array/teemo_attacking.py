def find_poisoned_duration(time_series, duration):
    seconds = 0

    if not time_series:
        return 0

    for i in range(len(time_series) - 1):
        seconds += min(time_series[i + 1] - time_series[i], duration)

    return seconds + duration


print(find_poisoned_duration([1, 4], 2))
print(find_poisoned_duration([1, 2], 2))
