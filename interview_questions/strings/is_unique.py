# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
# cannot use additional data structures?

def is_unique(s):
    if len(s) > 128:
        return False

    s_lst = []
    for char in s:
        if char in s_lst:
            return False
        s_lst.append(char)

    return True


# Time: O(n)
