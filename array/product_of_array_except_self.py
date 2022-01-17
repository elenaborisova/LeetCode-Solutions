def product_except_self(nums):
    ans = [1 for _ in nums]

    left = 1
    right = 1

    for i in range(len(nums)):
        ans[i] *= left
        ans[-1 - i] *= right
        left *= nums[i]
        right *= nums[-1 - i]

    return ans


def product_except_self2(nums):
    output = []

    p = 1
    for i in range(len(nums)):
        output.append(p)
        p *= nums[i]

    p = 1
    for i in range(len(nums) - 1, -1, -1):
        output[i] *= p
        p *= nums[i]

    return output


def product_except_self3(nums):
    prefix = []
    p = 1
    for i in range(len(nums)):
        prefix.append(p * nums[i])
        p *= nums[i]

    p = 1
    suffix = [None for _ in range(len(nums))]
    for i in range(len(nums) - 1, -1, -1):
        suffix[i] = p * nums[i]
        p *= nums[i]

    res = []
    for i in range(len(nums)):
        if i == 0:
            res.append(1 * suffix[i + 1])
        elif i == len(nums) - 1:
            res.append(prefix[i - 1] * 1)
        else:
            res.append(prefix[i - 1] * suffix[i + 1])

    return res


# Test cases:
print(product_except_self3([1, 2, 3, 4]))
