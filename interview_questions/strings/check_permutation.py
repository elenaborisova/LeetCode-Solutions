# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(s1, s2):
    if not len(s1) == len(s2):
        return False

    return sorted(s1) == sorted(s2)


# Time: n(log n log)
