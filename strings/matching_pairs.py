def count_matching_pairs(count, s, t):
    for i in range(len(s)):
        if s[i] == t[i]:
            count += 1
    return count


def matching_pairs(s, t):
    s, t = list(s), list(t)
    count = 0
    can_be_swapped = False

    if s == t or len(s) == 2:
        s[0], s[1] = s[1], s[0]
        return count_matching_pairs(count, s, t)

    for i in range(len(s)):
        if s[i] != t[i] and s[i] in t:
            t_index = t.index(s[i])
            can_be_swapped = True
            if s[t_index] == t[i]:
                s[t_index], s[i] = s[i], s[t_index]
                break
    else:
        if can_be_swapped:
            count += 1

    count = count_matching_pairs(count, s, t)
    return count


def matching_pairs2(s, t):
    combinations = []
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            combinations.append(''.join(s_list))
    print(combinations)

    maximum_combination = 0
    for word in combinations:
        count = 0
        for index in range(len(t)):
            if word[index] == t[index]:
                count += 1
        if count == len(t):
            return count
        if count > maximum_combination:
            maximum_combination = count
    return maximum_combination


# Test cases:
print(matching_pairs('abcd', 'adcb'))  # 4
print(matching_pairs('abcde', 'adcbe'))  # 5
print(matching_pairs('mno', 'mno'))  # 1
print(matching_pairs('abcde', 'ajcke'))  # 3
print(matching_pairs('abcd', 'abcd'))  # 2
print(matching_pairs('abcde', 'adcjb'))  # 3
print(matching_pairs('abcdefmn', 'ajcdbfnm'))  # 6
print(matching_pairs('xabcdy', 'vadcbw'))  # 4
print(matching_pairs('abcd', 'efgh'))  # 0
print(matching_pairs('abcdefghi', 'abcdefghi'))  # 7
print(matching_pairs('vjdkfa', 'alskdj'))  # 2
print(matching_pairs('laskdj', 'vjdkfa'))  # 3
print(matching_pairs('aaaa', 'aaaa'))  # 4
print(matching_pairs('ax', 'ay'))  # 0
print(matching_pairs('axb', 'ayb'))  # 1 WRONG
print(matching_pairs('axa', 'aya'))  # 2
print(matching_pairs('abx', 'abb'))  # 2
print(matching_pairs('abb', 'axb'))  # 2 WRONG
print(matching_pairs('ax', 'ya'))  # 1
