def max_product(nums):
    res = max(nums)
    cur_min, cur_max = 1, 1

    for n in nums:
        tmp = cur_max * n
        cur_max = max(cur_max * n, cur_min * n, n)
        cur_min = min(tmp, cur_min * n, n)
        res = max(res, cur_max)

    return res


# Test cases:
print(max_product([2, 3, -2, 4]))
print(max_product([-2, 0, -1]))
print(max_product([-2, 3, -4]))
print(max_product([2, -5, -2, -4, 3]))
