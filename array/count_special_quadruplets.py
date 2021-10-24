def count_quadruplets(nums):
    n = len(nums)
    quadruplets_count = 0

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] == nums[l]:
                        quadruplets_count += 1

    return quadruplets_count


print(count_quadruplets([1, 1, 1, 3, 5]))
