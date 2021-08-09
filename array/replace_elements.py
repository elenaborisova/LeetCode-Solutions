def replace_elements(arr):
    replaced_elements = []

    for i in range(len(arr) - 1):
        greatest_right = max(arr[i + 1:])
        replaced_elements.append(greatest_right)

    return replaced_elements + [-1]


print(replace_elements([17, 18, 5, 4, 6, 1]))
print(replace_elements([400]))
