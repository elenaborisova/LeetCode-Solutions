def check_when_same_length(s, t):
    difference_count = 0
    for i in range(len(s)):
        if not s[i] == t[i]:
            difference_count += 1
        if difference_count > 1:
            return False
    return True


def check_when_diff_length(s1, s2):
    s1_idx = 0
    s2_idx = 0
    diff_count = 0

    while s1_idx < len(s1) and s2_idx < len(s2):
        if not s1[s1_idx] == s2[s2_idx]:
            s1_idx += 1
            diff_count += 1
        else:
            s2_idx += 1
            s1_idx += 1

        if diff_count > 1:
            return False

    return True


def is_one_away(s, t):
    s_len = len(s)
    t_len = len(t)

    if abs(s_len - t_len) > 1:
        return False

    if s_len == t_len:
        return check_when_same_length(s, t)
    elif s_len < t_len:
        return check_when_diff_length(t, s)
    else:
        return check_when_diff_length(s, t)


print(is_one_away('pale', 'ple'))
print(is_one_away('pales', 'pale'))
print(is_one_away('pale', 'bale'))
print(is_one_away('pale', 'bake'))
print(is_one_away('aab', 'abc'))
