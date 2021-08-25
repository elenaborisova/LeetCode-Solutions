def common_chars(words):
    common = []

    for char in words[0]:
        for i in range(1, len(words)):
            if char not in words[i]:
                break
            else:
                words[i] = words[i].replace(char, '', 1)
        else:
            common.append(char)

    return common


print(common_chars(["bella", "label", "roller"]))
print(common_chars(["cool", "lock", "cook"]))
