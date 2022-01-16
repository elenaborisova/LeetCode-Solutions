def single_number(nums):
    nums.sort()

    for i in range(1, len(nums), 2):
        if nums[i] != nums[i - 1]:
            return nums[i - 1]

    return nums[-1]


def single_number2(nums):
    return sum(set(nums)) * 2 - sum(nums)


def single_number3(nums):
    n = nums[0]

    for i in range(1, len(nums)):
        n = n ^ nums[i]

    return n


# Test cases:
print(single_number2([2, 2, 1]))
print(single_number3([4, 1, 2, 1, 2]))
print(single_number2([1]))
