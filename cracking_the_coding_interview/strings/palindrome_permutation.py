# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def is_permutation_of_palindrome(s):
    s = s.lower()
    chars_count = {}
    odd_counts = 0

    for char in s:
        if char == ' ':
            continue
        if char not in chars_count:
            chars_count[char] = 0
        chars_count[char] += 1

    for count in chars_count.values():
        if count % 2 == 1:
            odd_counts += 1
        if odd_counts > 1:
            return False

    return True


print(is_permutation_of_palindrome('Aaaaaab'))

# Time: O(n)
