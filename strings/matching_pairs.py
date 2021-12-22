def matching_pairs(s, t):
    combinations = []
    maximum_combination = 0

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s_list = list(s)
            s_list[i], s_list[j] = s_list[j], s_list[i]
            combinations.append(s_list)

    for word in combinations:
        count = 0
        for index in range(len(t)):
            if word[index] == t[index]:
                count += 1
        if count == len(t):
            return count

        maximum_combination = max(count, maximum_combination)

    return maximum_combination


# Test cases:
print(matching_pairs('abcd', 'adcb') == 4)
print(matching_pairs('abcde', 'adcbe') == 5)
print(matching_pairs('mno', 'mno') == 1)
print(matching_pairs('abcde', 'ajcke') == 3)
print(matching_pairs('abcd', 'abcd') == 2)
print(matching_pairs('abcde', 'adcjb') == 3)
print(matching_pairs('abcdefmn', 'ajcdbfnm') == 6)
print(matching_pairs('xabcdy', 'vadcbw') == 4)
print(matching_pairs('abcd', 'efgh') == 0)
print(matching_pairs('abcdefghi', 'abcdefghi') == 7)
print(matching_pairs('vjdkfa', 'alskdj') == 2)
print(matching_pairs('laskdj', 'vjdkfa') == 3)
print(matching_pairs('aaaa', 'aaaa') == 4)
print(matching_pairs('ax', 'ay') == 0)
print(matching_pairs('axb', 'ayb') == 1)
print(matching_pairs('axa', 'aya') == 2)
print(matching_pairs('abx', 'abb') == 2)
print(matching_pairs('abb', 'axb') == 2)
print(matching_pairs('ax', 'ya') == 1)
