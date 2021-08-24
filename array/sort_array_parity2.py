def sort_array_by_parity(nums):
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]
    sorted_nums = []

    for i in range(len(nums)):
        if i % 2 == 0:
            sorted_nums.append(even_nums.pop(0))
        else:
            sorted_nums.append(odd_nums.pop(0))

    return sorted_nums


print(sort_array_by_parity([4, 2, 5, 7]))
print(sort_array_by_parity([2, 3]))
