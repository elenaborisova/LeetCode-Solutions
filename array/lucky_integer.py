def find_lucky(arr):
    arr.sort(reverse=True)
    lucky_integer = -1

    for num in arr:
        if arr.count(num) == num:
            lucky_integer = max(lucky_integer, num)
            break

    return lucky_integer


print(find_lucky([2, 2, 3, 4]))
print(find_lucky([1, 2, 2, 3, 3, 3]))
print(find_lucky([2, 2, 2, 3, 3]))
print(find_lucky([7, 7, 7, 7, 7, 7, 7]))
