def three_consecutive_odds(arr):
    for i in range(2, len(arr)):
        if arr[i] % 2 == 1 and arr[i - 1] % 2 == 1 and arr[i - 2] % 2 == 1:
            return True
    return False


print(three_consecutive_odds([2, 6, 4, 1]))
print(three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
print(three_consecutive_odds([1, 1, 1]))
