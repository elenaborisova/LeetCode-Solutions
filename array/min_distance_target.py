def get_min_distance(nums, target, start):
    min_distance = 10000

    for i in range(len(nums)):
        if nums[i] == target:
            curr_distance = abs(i - start)
            min_distance = min(curr_distance, min_distance)

    return min_distance


print(get_min_distance(nums=[1, 2, 3, 4, 5], target=5, start=3))
print(get_min_distance(nums=[1], target=1, start=0))
print(get_min_distance(nums=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], target=1, start=0))
