def repeated_n_times(nums):
    # nums.length == 2 * n
    n = len(nums) // 2

    for num in nums:
        if nums.count(num) == n:
            return num


print(repeated_n_times([1, 2, 3, 3]))
print(repeated_n_times([2, 1, 2, 5, 3, 2]))
print(repeated_n_times([5, 1, 5, 2, 5, 3, 5, 4]))
