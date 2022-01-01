import collections


def min_length_substrings(s, t):
    pass


def sliding_window(s, t):
    if not s or not t or len(t) > len(s):
        return ''

    dict_t = collections.Counter(t)
    required = len(dict_t)
    l, r = 0, 0
    formed = 0
    window_counts = {}
    ans = float("inf"), None, None

    while r < len(s):
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        while l <= r and formed == required:
            character = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            l += 1
        r += 1

    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]


print(sliding_window('dcbefebce', 'fd'))
print(sliding_window('bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf', 'cbccfafebccdccebdd'))
print(sliding_window('baaaab', 'bb'))
print(sliding_window('aaaaa', 'a'))
print(sliding_window('aja', 'j'))
print(sliding_window('dcbeffebce', 'fd'))
print(sliding_window('dcbeffebce', 'fdf'))
print(sliding_window('bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf', 'cbccfafebccdccebff'))
print(sliding_window('a', 'a'))
print(sliding_window('ADOBECODEBANC', 'ABC'))
print(sliding_window('a', 'aa'))
print(sliding_window('ABAACBAB', 'ABC'))
