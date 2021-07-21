def max_profit(prices):
    max_p = 0
    buy = 10 ** 4
    sell = -100000
    buy_i = 0
    sell_i = 0

    for i in range(len(prices)):
        if prices[i] < buy:
            buy = prices[i]
            buy_i = i

        if prices[i] > buy:
            sell = prices[i]
            sell_i = i

        if sell - buy > max_p and buy_i < sell_i:
            max_p = sell - buy

    return max_p


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7,6,4,3,1]))
print(max_profit([1, 2]))
print(max_profit([2, 4, 1]))