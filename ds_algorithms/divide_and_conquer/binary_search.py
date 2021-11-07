def binary(lst, value):
    left_pivot = 0
    right_pivot = len(lst) - 1
    middle = (right_pivot + left_pivot) // 2

    while left_pivot <= right_pivot:
        middle = (right_pivot + left_pivot) // 2
        if lst[middle] == value:
            return True
        elif lst[middle] < value:
            left_pivot = middle + 1
        else:
            right_pivot = middle - 1

    return False
