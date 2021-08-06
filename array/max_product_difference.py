def max_product_difference(nums):
    first_pair = [nums.pop(nums.index(max(nums))), max(nums)]
    second_pair = [nums.pop(nums.index(min(nums))), min(nums)]
    difference = (first_pair[0] * first_pair[1]) - (second_pair[0] * second_pair[1])

    return difference


print(max_product_difference([5, 6, 2, 7, 4]))
print(max_product_difference([4, 2, 5, 9, 7, 4, 8]))
