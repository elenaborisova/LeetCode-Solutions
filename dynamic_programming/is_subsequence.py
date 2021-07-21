def is_subsequence(s, t):
    chars = []

    i = 0
    while t and i < len(s):
        sub_char = s[i]

        if sub_char not in t:
            return False

        chars.append(sub_char)
        char_idx = t.index(sub_char)
        t = t[char_idx+1:]
        i += 1

    if ''.join(chars) == s:
        return True
    return False


print(is_subsequence('acea', 'abcdea'))
print(is_subsequence('axc', 'ahbgdc'))
print(is_subsequence('abc', 'ahbgdc'))
print(is_subsequence('aaaaaa', 'bbaaaa'))
print(is_subsequence('ab', 'baab'))
print(is_subsequence('', 'ahbgdc'))
print(is_subsequence('b', 'abc'))
