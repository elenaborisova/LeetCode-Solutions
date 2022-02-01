def two_sum(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1


# Test cases:
print(two_sum(numbers=[2, 7, 11, 15], target=9))
print(two_sum(numbers=[2, 3, 4], target=6))
print(two_sum(numbers=[-1, 0], target=-1))
print(two_sum([0, 0, 3, 4], 0))
