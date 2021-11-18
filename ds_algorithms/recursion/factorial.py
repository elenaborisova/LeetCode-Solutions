# Recursive approach - Time: O(n); Space: O(n)
def factorial(n):
    if n < 0:
        raise ValueError('Inputs 0 or greater only')

    if n <= 1:
        return n

    return n * factorial(n - 1)


# Iterative approach - Time: O(n); Space: O(1)
def factorial2(n):
    res = 1
    for i in range(2, n + 1):
        res *= i

    return res
