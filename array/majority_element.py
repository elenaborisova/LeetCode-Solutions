def majority_element(nums):
    threshold = len(nums) // 2

    for num in set(nums):
        if nums.count(num) > threshold:
            return num


print(majority_element([3, 2, 3]))
print(majority_element([2, 2, 1, 1, 1, 2, 2]))
