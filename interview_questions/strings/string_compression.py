# String Compression: Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).


def compress_string(s):
    compressed_chars = []
    count = 1
    compressed_is_smaller = False

    for i in range(len(s)):
        if i == len(s) - 1 or not s[i] == s[i + 1]:
            compressed_chars.append(s[i])
            compressed_chars.append(str(count))
            count = 1
        else:
            count += 1
            compressed_is_smaller = True

    compressed_s = ''.join(compressed_chars)
    return compressed_s if compressed_is_smaller else s


print(compress_string('aabcccccaaa'))
print(compress_string('abcd'))

# Time complexity: O(n)
