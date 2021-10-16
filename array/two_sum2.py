def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1


print(two_sum(numbers=[1, 2, 7, 11, 15], target=9))
print(two_sum(numbers=[2, 3, 4], target=6))
print(two_sum(numbers=[-1, 0], target=-1))
print(two_sum([0, 0, 3, 4], 0))