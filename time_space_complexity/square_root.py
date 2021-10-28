def sqrt(n):
    for guess in range(n):
        if guess * guess == n:
            return guess
    return -1
