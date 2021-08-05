def maximum_wealth(accounts):
    max_wealth = 0

    for account in accounts:
        curr_wealth = sum(account)
        if max_wealth < curr_wealth:
            max_wealth = curr_wealth

    return max_wealth


print(maximum_wealth([[1, 2, 3], [3, 2, 1]]))
print(maximum_wealth([[1, 5], [7, 3], [3, 5]]))
print(maximum_wealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]]))
