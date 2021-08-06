def count_consistent_strings(allowed, words):
    count = 0

    for word in words:
        for char in word:
            if char not in allowed:
                break
        else:
            count += 1

    return count


print(count_consistent_strings("ab", ["ad", "bd", "aaab", "baa", "badab"]))
print(count_consistent_strings("abc", ["a", "b", "c", "ab", "ac", "bc", "abc"]))
print(count_consistent_strings("cad", ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]))
