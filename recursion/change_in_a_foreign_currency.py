def can_get_exact_change(target_money, denominations):
    if target_money == 0:
        return True

    for d in denominations:
        if d <= target_money:
            if can_get_exact_change(target_money - d, denominations):
                return True

    return False


# Test cases:
print(can_get_exact_change(75, [4, 17, 29]) == True)
print(can_get_exact_change(7, [1, 5, 10]) == True)
print(can_get_exact_change(94, [5, 10, 25, 100, 200]) == False)
print(can_get_exact_change(20, [200]) == False)
print(can_get_exact_change(96, [6, 10, 25, 100, 200]) == True)
print(can_get_exact_change(96, [10, 25, 100, 200]) == False)
print(can_get_exact_change(97, [10, 15, 17]) == True)  # False
print(can_get_exact_change(8, [3, 5, 6]) == True)
print(can_get_exact_change(21, [20, 7]) == True)
