def find_kth_positive(arr, k):
    counter = 0
    i = 1

    while True:
        if i not in arr:
            counter += 1

        if counter == k:
            return i

        i += 1


print(find_kth_positive([2, 3, 4, 7, 11], 5))
print(find_kth_positive([1, 2, 3, 4], 2))
