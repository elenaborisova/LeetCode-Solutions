def find_shortest_subarray(nums):
    degrees = {}
    shortest_array_len = len(nums)

    for num in nums:
        if num not in degrees:
            degrees[num] = 0
        degrees[num] += 1

    max_degree = max(degrees.values())

    for num, degree in degrees.items():
        if degree == max_degree:
            first_num = nums.index(num)
            last_num = len(nums) - nums[::-1].index(num) - 1
            shortest_array_len = min(shortest_array_len, len(nums[first_num:last_num + 1]))

    return shortest_array_len


print(find_shortest_subarray([1, 2, 2, 3, 1]))
print(find_shortest_subarray([1, 2, 2, 3, 1, 4, 2]))
