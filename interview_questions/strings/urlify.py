# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
# has sufficient space at the end to hold the additional characters, and that you are given the "true"
# length of the string. (Note: If implementing in Java, please use a character array so that you can
# perform this operation in place.)

def urlify(s, length):
    res = []

    for i in range(length):
        if s[i] == ' ':
            res.append('%20')
        else:
            res.append(s[i])

    return ''.join(res)


print(urlify("Mr John Smith ", 13))

# Time: O(n)
