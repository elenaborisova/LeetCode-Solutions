def max_profit(prices):
    max_p = 0

    i = 0
    while i < len(prices) - 1:
        while i < len(prices) - 1 and prices[i] >= prices[i + 1]:
            i += 1

        valley = prices[i]

        while i < len(prices) - 1 and prices[i] <= prices[i + 1]:
            i += 1

        peak = prices[i]
        max_p += peak - valley

    return max_p


# Test cases:
print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([1, 2]))
print(max_profit([2, 4, 1]))
print(max_profit([1, 2, 3, 4, 5]))
print(max_profit([6, 1, 3, 2, 4, 7]))
