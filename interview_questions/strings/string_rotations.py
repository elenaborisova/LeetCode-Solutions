# String Rotation: Assume you have a method isSubstringwhich checks if one word is a substring
# of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")

def is_substring(s1, s2):
    return s2 in s1


def is_string_rotation(s1, s2):
    if not len(s1) == len(s2):
        return False

    double_s1 = s1 + s1
    return is_substring(double_s1, s2)


print(is_string_rotation('waterbottle', 'erbottlewat'))

# Time: O(n)
