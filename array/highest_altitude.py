def largest_altitude(gain):
    altitudes = [0, gain[0]]

    for i in range(1, len(gain)):
        curr_altitude = altitudes[i] + gain[i]
        altitudes.append(curr_altitude)

    return max(altitudes)


print(largest_altitude([-5, 1, 5, 0, -7]))
print(largest_altitude([-4, -3, -2, -1, 4, 3, 2]))
