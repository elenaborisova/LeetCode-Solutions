def relative_sort_array(arr1, arr2):
    sorted_array = []

    for el in arr2:
        while el in arr1:
            sorted_array.append(arr1.pop(arr1.index(el)))

    sorted_array += sorted(arr1)

    return sorted_array


print(relative_sort_array([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
print(relative_sort_array([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
