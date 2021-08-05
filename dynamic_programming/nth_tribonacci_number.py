def tribonacci(n):
    t0 = 0
    t1 = 1
    t2 = 1
    t = 0

    if n == 1 or n == 2:
        return 1

    for i in range(3, n+1):
        t = t0 + t1 + t2
        t0 = t1
        t1 = t2
        t2 = t

    return t


print(tribonacci(3))
