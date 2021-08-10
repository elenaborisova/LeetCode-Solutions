def can_be_equal(target, arr):
    return sorted(target) == sorted(arr)


print(can_be_equal(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
print(can_be_equal(target=[3, 7, 9], arr=[3, 7, 11]))
