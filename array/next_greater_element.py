def next_greater_element(arr1, arr2):
    result = []

    for i in range(len(arr1)):
        num = arr1[i]
        arr2_idx = arr2.index(num)

        for j in range(arr2_idx + 1, len(arr2)):
            num2 = arr2[j]
            if num2 > num:
                result.append(num2)
                break
        else:
            result.append(-1)

    return result


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_element([2, 4], [1, 2, 3, 4]))
