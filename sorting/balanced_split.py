def balanced_split_exists(arr):
    if len(arr) < 2 or sum(arr) % 2 != 0:
        return False

    arr.sort()  # n log n
    l, r = 0, len(arr) - 1
    left_sum, right_sum = arr[l], arr[r]

    while l <= r:
        if arr[l] >= arr[r]:
            return False

        if left_sum < right_sum:
            l += 1
            left_sum += arr[l]
        elif right_sum < left_sum:
            r -= 1
            right_sum += arr[r]
        else:
            l += 1
            r -= 1
            left_sum += arr[l]
            right_sum += arr[r]

    return True


# Test cases:
print(balanced_split_exists([5, 5]) == False)
print(balanced_split_exists([1, 5, 7, 1]) == True)
print(balanced_split_exists([12, 7, 6, 7, 6]) == False)
print(balanced_split_exists([2, 1, 2, 5]) == True)
print(balanced_split_exists([3, 6, 3, 4, 4]) == False)

print(balanced_split_exists([]) == False)
print(balanced_split_exists([0]) == False)
print(balanced_split_exists([1, 5, 4]) == True)
print(balanced_split_exists([5, 1, 6, 5, 5]) == False)

print(balanced_split_exists([0, 1, 0, 2, 3, 4]) == False)
print(balanced_split_exists([0, 1, 4, 4, 2, 3]) == False)
print(balanced_split_exists([1, 1, 1, 1, 1, 2, 3]) == True)
print(balanced_split_exists([1, 1, 1, 1, 1, 2, 3, 4]) == True)
print(balanced_split_exists([1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4]) == True)
print(balanced_split_exists([4, 4, 4, 4, 4, 4, 8, 8, 8]) == True)

print(balanced_split_exists([5, 7, 20, 12, 5, 7, 6, 14, 5, 5, 6]) == True)
print(balanced_split_exists([5, 7, 20, 12, 5, 7, 6, 7, 14, 5, 5, 6]) == False)
print(balanced_split_exists([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == False)
