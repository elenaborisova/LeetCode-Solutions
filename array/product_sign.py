def array_sign(nums):
    product = 1

    for num in nums:
        if num == 0:
            return 0
        product *= num

    if product > 0:
        return 1
    else:
        return -1


print(array_sign([-1, -2, -3, -4, 3, 2, 1]))
print(array_sign([1, 5, 0, 2, -3]))
print(array_sign([-1, 1, -1, 1, -1]))
