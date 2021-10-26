def func1(a, b, array):
    # O(n) time

    min_value = a
    max_value = b

    for x in array:
        if x < min_value:
            min_value = x
        elif x > max_value:
            max_value = x


def func2(a, b, array):
    # O(n) time

    min_value = a
    max_value = b

    for x in array:
        if x < min_value:
            min_value = x
    
    for x in array:
        if x > max_value:
            max_value = x

