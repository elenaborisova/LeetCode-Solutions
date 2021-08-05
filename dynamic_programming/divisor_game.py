def divisor_game(n):
    i = -1  # even Alice, odd Bob
    while True:
        for x in range(1, n):
            if n % x == 0:
                n -= x
                i += 1
                break
        else:
            if i % 2 == 0:
                return True
            return False


print(divisor_game(3))
