def can_make_arithmetic_progression(arr):
    arr = sorted(arr)
    prev_diff = arr[1] - arr[0]

    for i in range(1, len(arr)):
        difference = arr[i] - arr[i - 1]

        if not difference == prev_diff:
            return False

        prev_diff = difference

    return True


print(can_make_arithmetic_progression([3, 5, 1]))
print(can_make_arithmetic_progression([1, 2, 4]))
