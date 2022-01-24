def find_min(nums):
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        mid = (l + r) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return res


def find_min2(nums):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if l == r:
            return nums[0]

        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return min(nums[0], nums[mid + 1])

        if nums[l] < nums[mid]:
            l = mid
        else:
            r = mid

    return nums[0]


# Test cases:
print(find_min([3, 4, 5, 1, 2]))
print(find_min([4, 5, 6, 7, 0, 1, 2]))
print(find_min([11, 13, 15, 17]))
print(find_min([1]))
print(find_min([3, 1, 2]))
print(find_min([5, 1, 2, 3, 4]))
