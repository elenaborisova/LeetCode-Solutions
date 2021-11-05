def is_one_away(s, t):
    s_len = len(s)
    t_len = len(t)

    if abs(s_len - t_len) > 1:
        return False

    if s_len == t_len:
        difference_count = 0
        for i in range(s_len):
            if not s[i] == t[i]:
                difference_count += 1
            if difference_count > 1:
                return False
        return True

    if s_len < t_len:
        s_idx = 0
        t_idx = 0
        diff_count = 0
        while s_idx < s_len and t_idx < t_len:
            if not s[s_idx] == t[t_idx]:
                t_idx += 1
                diff_count += 1
            else:
                t_idx += 1
                s_idx += 1

            if diff_count > 1:
                return False


print(is_one_away('pale', 'ple'))
print(is_one_away('pales', 'pale'))
print(is_one_away('pale', 'bale'))
print(is_one_away('pale', 'bake'))
print(is_one_away('aab', 'abc'))
