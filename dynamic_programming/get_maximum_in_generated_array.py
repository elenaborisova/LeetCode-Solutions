def get_maximum_generated(n):
    generated_array = [0, 1]

    if n == 0:
        return 0

    i = 2
    while len(generated_array) < n:
        num = generated_array[i - 1]
        generated_array.append(num)

        num = generated_array[i] + generated_array[i - 1]
        generated_array.append(num)

        i += 1

    return max(generated_array)


print(get_maximum_generated(7))
print(get_maximum_generated(2))
print(get_maximum_generated(3))
print(get_maximum_generated(0))
