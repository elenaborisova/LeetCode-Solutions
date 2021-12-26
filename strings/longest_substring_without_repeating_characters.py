def length_of_longest_substring(s):
    l, r, max_len = 0, 0, 0

    while r < len(s):
        substring = s[l:r + 1]
        max_len = max(max_len, len(substring))

        if r + 1 < len(s) and s[r + 1] in substring:
            l += 1
        else:
            r += 1

    return max_len


def length_of_longest_substring_optimized(s):
    used = {}
    max_length = start = 0

    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[c] = i

    return max_length


# Test cases:
print(length_of_longest_substring('abcabcbb') == 3)
print(length_of_longest_substring('bbbbb') == 1)
print(length_of_longest_substring('pwwkew') == 3)
