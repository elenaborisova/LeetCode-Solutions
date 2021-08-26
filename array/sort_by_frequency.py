def frequency_sort(nums):
    frequency = {}

    for num in nums:
        if num not in frequency:
            frequency[num] = 1
        else:
            frequency[num] += 1

    sorted_frequency = dict(sorted(frequency.items(), key=lambda x: (x[1], -x[0])))
    sorted_list = [k for k, v in sorted_frequency.items() for _ in range(v)]

    return sorted_list


print(frequency_sort([1, 1, 2, 2, 2, 3]))
print(frequency_sort([2, 3, 1, 3, 2]))
print(frequency_sort([-1, 1, -6, 4, 5, -6, 1, 4, 1]))
