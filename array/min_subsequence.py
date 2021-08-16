def min_subsequence(nums):
    nums = sorted(nums, reverse=True)
    subsequence = []
    sum_subsequence = 0
    sum_nums = sum(nums)

    i = 0
    while True:
        max_el = nums[i]
        subsequence.append(max_el)
        sum_subsequence += max_el
        sum_nums -= max_el
        i += 1

        if sum_subsequence > sum_nums:
            break

    return subsequence


print(min_subsequence([4, 3, 10, 9, 8]))
print(min_subsequence([4, 4, 7, 6, 7]))
print(min_subsequence([6]))
