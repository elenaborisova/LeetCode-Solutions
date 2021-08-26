def single_number(nums):
    frequency = {}

    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    frequency = dict(sorted(frequency.items(), key=lambda x: x[1]))
    return next(iter(frequency))


print(single_number([2, 2, 1]))
print(single_number([4, 1, 2, 1, 2]))
print(single_number([1]))
