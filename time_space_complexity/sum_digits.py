def sum_digits(n):
    # Time: O(log n)

    total_sum = 0
    while n > 0:
        total_sum += n % 10
        n //= 10

    return total_sum


print(sum_digits(111))
