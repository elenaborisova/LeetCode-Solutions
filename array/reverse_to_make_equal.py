def are_they_equal(array_a, array_b):
    if array_a == array_b:
        return True

    subarray = []
    indices = []

    i = 0
    while i < len(array_a):
        if array_b[i] != array_a[i]:
            subarray.append(array_b[i])
            indices.append(i)

        while subarray:
            i += 1
            subarray.append(array_b[i])
            indices.append(i)

            if subarray[::-1] == array_a[indices[0]:indices[-1] + 1]:
                array_b = array_b[:indices[0]] + subarray[::-1] + array_b[indices[-1] + 1:]
                subarray = []
                break

        i += 1

    if array_a == array_b:
        return True
    return False


def reverse_to_make_equal2(array_a, array_b):
    return sorted(array_a) == sorted(array_b)


print(are_they_equal([1, 2, 3, 4, 5], [1, 4, 3, 2, 5]))
