import collections


def min_length_substrings(s, t):
    pass


def sliding_window(s, t):
    if not s or not t or len(t) > len(s):
        return ''

    dict_t = collections.Counter(t)

    # Number of unique characters in t, which need to be present in the desired window.
    required = len(dict_t)

    # left and right pointer
    l, r = 0, 0

    # formed is used to keep track of how many unique characters in t are present in the current window in its desired frequency.
    formed = 0

    # Dictionary which keeps a count of all the unique characters in the current window.
    window_counts = {}

    # ans tuple of the form (window length, left, right)
    ans = float("inf"), None, None

    while r < len(s):

        # Add one character from the right to the window
        character = s[r]
        window_counts[character] = window_counts.get(character, 0) + 1

        # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
        if character in dict_t and window_counts[character] == dict_t[character]:
            formed += 1

        # Try and contract the window till the point where it ceases to be 'desirable'.
        while l <= r and formed == required:
            character = s[l]

            # Save the smallest window until now.
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # The character at the position pointed by the `left` pointer is no longer a part of the window.
            window_counts[character] -= 1
            if character in dict_t and window_counts[character] < dict_t[character]:
                formed -= 1

            # Move the left pointer ahead, this would help to look for a new window.
            l += 1

            # Keep expanding the window once we are done contracting.
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
