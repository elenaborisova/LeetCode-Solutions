# Recursive approach - Time: O(2^n); Space: O(n)
def fibonacci(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Iterative approach - Time: O(n); Space: O(1)
def fibonacci2(n):
    if n < 0:
        raise ValueError()

    if n <= 1:
        return 0

    if n == 2:
        return 1

    prev2 = 0
    prev1 = 1
    current = None

    for i in range(2, n + 1):
        current = prev2 + prev1
        prev2 = prev1
        prev1 = current

    return current
