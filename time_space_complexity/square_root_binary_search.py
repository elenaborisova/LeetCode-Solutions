def sqrt(n):
    return sqrt_helper(n, 1, n)


def sqrt_helper(n, min, max):
    # Time: O(log n)
    if max < min:
        return -1  # no square root

    guess = (min + max) // 2

    if guess * guess == n:
        return guess  # found it!
    elif guess * guess < n:
        return sqrt_helper(n, guess + 1, max)  # try higher
    else:
        return sqrt_helper(n, min, guess - 1)  # try lower
