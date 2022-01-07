def is_palindrome(s):
    # Time: O(n); Space: O(n)

    s_lst = []
    for char in s:
        if char.isalnum():
            s_lst.append(char.lower())
    new_s = ''.join(s_lst)

    i, j = 0, len(new_s) - 1
    while i < j:
        if new_s[i] != new_s[j]:
            return False
        i += 1
        j -= 1

    return True


def is_palindrome2(s):
    # Time: O(n); Space: O(n)

    s_lst = []
    for char in s:
        if char.isalnum():
            s_lst.append(char.lower())
    new_s = ''.join(s_lst)

    return new_s == new_s[::-1]


def is_palindrome_inplace(s):
    # Time: O(n); Space: O(1)

    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif not s[i].lower() == s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True


# Test cases:
print(is_palindrome_inplace('A man, a plan, a canal: Panama') == True)
print(is_palindrome_inplace('race a car') == False)
print(is_palindrome_inplace(' ') == True)
print(is_palindrome_inplace('0P') == False)
