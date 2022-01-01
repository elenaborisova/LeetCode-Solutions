def find_encrypted_word(s):
    r = ''

    if len(s) <= 2:
        return s

    if len(s) % 2 == 0:
        mid = len(s) // 2 - 1
    else:
        mid = len(s) // 2

    r += s[mid]
    r += find_encrypted_word(s[:mid])
    r += find_encrypted_word(s[mid + 1:])

    return r


# Test cases:
print(find_encrypted_word('abc') == 'bac')
print(find_encrypted_word('abcd') == 'bacd')
print(find_encrypted_word('abcxcba') == 'xbacbca')
print(find_encrypted_word('facebook') == 'eafcobok')
print(find_encrypted_word('abcabcabcabc') == 'ccababcabbac')
