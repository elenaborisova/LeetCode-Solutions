# Best case (time complexity): n(0); worst case:
def pattern_search(text, pattern):
    for index in range(len(text) - len(pattern) + 1):
        match_count = 0
        print('first', index)

        for char in range(len(pattern)):
            print('here', char)
            if pattern[char] == text[index + char]:
                match_count += 1
            else:
                break

        if match_count == len(pattern):
            print(pattern, "found at index", index)


text = "AAAA"
pattern = "AAAA"
pattern_search(text, pattern)
