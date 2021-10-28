def fib(n):
    # Time: O(2 ^ n) -> 2 branches of depth n
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


fib(5)
