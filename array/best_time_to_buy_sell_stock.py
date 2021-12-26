def max_profit(prices):
    # Brute Force; Time: O(n^2)

    max_p, i, j = 0, 0, 1

    while i < len(prices):
        while j < len(prices):
            profit = prices[j] - prices[i]
            max_p = max(max_p, profit)
            j += 1
        i += 1
        j = i + 1

    return max_p


def max_profit_optimized(prices):
    # Time: O(n)
    max_p = 0
    buy = 10 ** 4
    sell = -100000
    buy_i, sell_i = 0, 0

    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
            buy_i = i

        if prices[i] > buy:
            sell = prices[i]
            sell_i = i

        if buy_i < sell_i:
            max_p = max(max_p, sell - buy)

    return max_p


def max_profit_leetcode(prices):
    # Leetcode solution; Time: O(n)
    min_price = 10 ** 4
    max_p = 0

    for i in range(len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        elif prices[i] - min_price > max_p:
            max_p = prices[i] - min_price

    return max_p


# Test cases:
print(max_profit([7, 1, 5, 3, 6, 4]) == 5)
print(max_profit([7, 6, 4, 3, 1]) == 0)
print(max_profit([1, 4, 2]) == 3)
