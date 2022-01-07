def valid_palindrome(s):
    # Time: O(n); Space: O(n)

    i, j = 0, len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return s[i + 1:j + 1] == s[i + 1:j + 1][::-1] \
                   or s[i:j] == s[i:j][::-1]  # O(n) but happens a maximum of one time
        i += 1
        j -= 1

    return True


def valid_palindrome2(s):
    # Time: O(n); Space: O(1)

    i, j = 0, len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return check_palindrome(s, i + 1, j) or check_palindrome(s, i, j - 1)
        i += 1
        j -= 1

    return True


def check_palindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True


# Test cases:
print(valid_palindrome('aba') == True)
print(valid_palindrome('abca') == True)
print(valid_palindrome('abc') == False)
print(valid_palindrome('deeee') == True)
print(valid_palindrome('eeccccbebaeeabebccceea') == False)
print(valid_palindrome('eedede') == True)
