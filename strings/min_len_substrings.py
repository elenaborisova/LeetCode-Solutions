import collections


def min_length_substrings(s, t):
    if len(t) > len(s):
        return -1

    t_chars_count = {el: t.count(el) for el in t}
    min_len, i, j = 1000001, 0, 0

    while j < len(s):
        while i + len(t) <= len(s):
            subarray = s[j:i + len(t)]

            if all(el in subarray and subarray.count(el) >= t_chars_count[el] for el in t):
                min_len = min(len(subarray), min_len)
            i += 1

        j += 1
        i = j

    return min_len if min_len != 1000001 else -1


def sliding_window(s, t):
    if len(t) > len(s):
        return ''

    t_chars_count = collections.Counter(t)
    left, right = 0, 0
    contracting = False
    result = ''

    while right + len(t) <= len(s):
        substring = s[left:right + len(t)]

        if all(el in substring and substring.count(el) >= t_chars_count[el] for el in t):
            if not result or len(substring) < len(result):
                result = ''.join(substring)
            contracting = True
            left += 1
        elif not contracting:
            right += 1
        elif contracting:
            right += 1
            contracting = False

    return result


print(min_length_substrings('dcbefebce', 'fd'))
print(min_length_substrings('bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf', 'cbccfafebccdccebdd'))
print(min_length_substrings('baaaab', 'bb'))
print(min_length_substrings('aaaaa', 'a'))
print(min_length_substrings('aja', 'j'))
print(min_length_substrings('dcbeffebce', 'fd'))
print(min_length_substrings('dcbeffebce', 'fdf'))
print(min_length_substrings('bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf', 'cbccfafebccdccebff'))
print(min_length_substrings('a', 'a'))
print(min_length_substrings('ADOBECODEBANC', 'ABC'))
print(min_length_substrings('a', 'aa'))
print(min_length_substrings('ABAACBAB', 'ABC'))
