def slowest_key(release_times, keys_pressed):
    start_time = 0
    durations = []

    for i in range(len(keys_pressed)):
        release_time = release_times[i]
        curr_duration = release_time - start_time
        start_time = release_time

        durations.append(curr_duration)

    max_duration = max(durations)
    slowest_keys = [keys_pressed[i] for i in range(len(durations)) if durations[i] == max_duration]
    return sorted(slowest_keys)[-1]


print(slowest_key([9, 29, 49, 50], "cbcd"))
print(slowest_key([12, 23, 36, 46, 62], "spuda"))