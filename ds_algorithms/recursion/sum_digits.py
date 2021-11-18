# Recursive approach - Time: O(n); Space: O(n)
def sum_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        # every digit except the last
        return last_digit + sum_digits(n // 10)


sum_digits(5567)


# Iterative approach - Time: O(n); Space: O(1)
def sum_digits2(n):
    if n < 0:
        ValueError('Inputs 0 or greater only!')

    result = 0
    while n is not 0:
        result += n % 10
        n = n // 10
    return result + n
