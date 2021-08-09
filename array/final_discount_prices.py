def final_prices(prices):
    final_discounted_prices = []
    i = 0
    j = 1

    while i < len(prices):
        if j == len(prices):
            final_discounted_prices.append(prices[i])
            i += 1
            j = i + 1
        elif prices[j] <= prices[i]:
            discounted_price = prices[i] - prices[j]
            final_discounted_prices.append(discounted_price)
            i += 1
            j = i + 1
        else:
            j += 1

    return final_discounted_prices


print(final_prices([8, 4, 6, 2, 3]))
print(final_prices([1, 2, 3, 4, 5]))
print(final_prices([10, 1, 1, 6]))
