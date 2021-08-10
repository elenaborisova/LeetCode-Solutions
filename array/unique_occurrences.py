def unique_occurrences(arr):
    occurrences = {}

    for num in arr:
        current_occ = arr.count(num)
        if current_occ in occurrences and not num == occurrences[current_occ]:
            return False

        occurrences[current_occ] = num

    return True


print(unique_occurrences([1, 2, 2, 1, 1, 3]))
print(unique_occurrences([1, 2]))
print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
