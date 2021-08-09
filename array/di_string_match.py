def di_string_match(s):
    nums = [i for i in range(len(s) + 1)]
    perm = []

    for i in range(len(s)):
        if s[i] == 'I':
            min_num = nums.pop(nums.index(min(nums)))
            perm.append(min_num)
        elif s[i] == 'D':
            max_num = nums.pop(nums.index(max(nums)))
            perm.append(max_num)

    perm.append(nums[0])

    return perm


print(di_string_match("IDID"))
print(di_string_match("III"))
print(di_string_match("DDI"))