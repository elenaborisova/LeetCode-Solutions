def find_disappeared_numbers(nums):
    n = len(nums)
    nums = set(nums)
    target = set(num for num in range(1, n + 1))

    return list(target.difference(nums))


print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_disappeared_numbers([1, 1]))
