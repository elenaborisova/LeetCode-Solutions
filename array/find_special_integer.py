def find_special_integer(arr):
    times_threshold = int(len(arr) * 0.25)

    for num in set(arr):
        if arr.count(num) > times_threshold:
            return num


print(find_special_integer([1, 2, 2, 6, 6, 6, 6, 7, 10]))
print(find_special_integer([1, 1]))
