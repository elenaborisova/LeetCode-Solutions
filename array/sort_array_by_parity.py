def sort_array_by_parity(nums):
    odd_nums = [num for num in nums if num % 2 == 1]
    even_nums = [num for num in nums if num % 2 == 0]
    return even_nums + odd_nums


print(sort_array_by_parity([3, 1, 2, 4]))
print(sort_array_by_parity([0]))
