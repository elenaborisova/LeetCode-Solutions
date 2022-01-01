from collections import Counter


def is_anagram(s, t):
    # O(n log n)
    return sorted(s) == sorted(t)


def is_anagram2(s, t):
    # O(n)
    s_counter = Counter(s)
    t_counter = Counter(t)
    return s_counter == t_counter
