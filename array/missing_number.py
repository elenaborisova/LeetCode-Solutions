def missing_number(nums):
    for num in range(len(nums) + 1):
        if num not in nums:
            return num


print(missing_number([3, 0, 1]))
print(missing_number([0, 1]))
print(missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(missing_number([0]))
