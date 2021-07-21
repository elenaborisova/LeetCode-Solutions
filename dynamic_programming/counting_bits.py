def count_bits(n):
    ones_in_bits = []
    binary = []

    for i in range(n + 1):
        num = i
        while num > 0:
            remainder = num % 2
            binary.append(remainder)
            num //= 2

        ones_in_bits.append(binary.count(1))
        binary = []

    return ones_in_bits


print(count_bits(2))
print(count_bits(5))


