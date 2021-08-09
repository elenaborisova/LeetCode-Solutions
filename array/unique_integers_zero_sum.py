def sum_zero(n):
    unique_integers = []

    for i in range(-(n // 2), n // 2 + 1):
        if n % 2 == 0 and i == 0:
            continue
        unique_integers.append(i)

    return unique_integers


print(sum_zero(5))
print(sum_zero(6))
print(sum_zero(1))
print(sum_zero(3))
