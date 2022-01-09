# Fibonacci series, iterative, Time: O(n)
def climb_stairs(n):
    n1 = 0
    n2 = 1

    if n == n1 or n == n2:
        return n

    for i in range(n):
        nums_sum = n1 + n2
        n1 = n2
        n2 = nums_sum

    return n2


# Top-down, Fibonacci, recursive, Time: O(2 ^ n)
def climb_stairs1(n):
    if n == 1 or n == 2:
        return n

    return climb_stairs1(n - 1) + climb_stairs1(n - 2)


# Top-down, memoization
def climb_stairs2(n):
    dic = {1: 1, 2: 2}

    if n not in dic:
        dic[n] = climb_stairs2(n - 1) + climb_stairs2(n - 2)
    return dic[n]


# Bottom up, O(n) space
def climb_stairs3(n):
    if n == 1:
        return 1

    res = [0 for _ in range(n)]
    res[0], res[1] = 1, 2

    for i in range(2, n):
        res[i] = res[i - 1] + res[i - 2]

    return res[-1]


# Bottom up, constant space
def climb_stairs4(n):
    if n == 1:
        return 1

    a, b = 1, 2

    for i in range(2, n):
        tmp = b
        b = a+b
        a = tmp

    return b


# Test cases:
print(climb_stairs3(5))
