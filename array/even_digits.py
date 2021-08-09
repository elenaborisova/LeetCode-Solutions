def find_numbers(nums):
    even_digits_count = 0

    for num in nums:
        if len(str(num)) % 2 == 0:
            even_digits_count += 1

    return even_digits_count


print(find_numbers([12, 345, 2, 6, 7896]))
print(find_numbers([555, 901, 482, 1771]))