def can_get_exact_change(target_money, denominations):
    if target_money == 0:
        return True

    for i in range(len(denominations) - 1, -1, -1):
        d = denominations[i]
        if d <= target_money:
            if can_get_exact_change(target_money % d, denominations[:i]):
                return True

    return False


def can_get_exact_change_iterative(target_money, denominations):
    denominations.sort()

    for i in range(len(denominations) - 1, -1, -1):
        d = denominations[i]
        if target_money % d == 0:
            return True
        else:
            target_money %= d

    return False


print(can_get_exact_change(75, [4, 17, 29]) == True)
print(can_get_exact_change(7, [1, 5, 10]) == True)
print(can_get_exact_change(94, [5, 10, 25, 100, 200]) == False)
print(can_get_exact_change(20, [200]) == False)
print(can_get_exact_change(1000000, [3, 6, 9, 12, 15]) == False)
print(can_get_exact_change(999999,
                           [54, 52, 50, 48, 46, 44, 42, 40, 38, 36, 34, 32, 30, 28, 26, 24, 22, 20, 18, 16, 14, 12, 10,
                            8, 6, 4, 2]) == False)
print(can_get_exact_change(96, [6, 10, 25, 100, 200]) == True)
print(can_get_exact_change(96, [10, 25, 100, 200]) == False)
print(can_get_exact_change(97, [10, 15, 17]) == True)  # False
print(can_get_exact_change(8, [3, 5, 6]) == True)
print(can_get_exact_change(21, [20, 7]) == True)
