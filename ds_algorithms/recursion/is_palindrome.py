# Recursive approach - Time: O(n); Space: O(n)
def is_palindrome(my_string):
    if len(my_string) <= 1:
        return True

    return my_string[0] == my_string[-1] and is_palindrome(my_string[1:-1])


# Iterative approach - Time: O(n^2); Space: O(n)
def is_palindrome2(my_string):
    while len(my_string) > 1:
        if my_string[0] != my_string[-1]:
            return False
        my_string = my_string[1:-1]
    return True


# More optimal iterative approach - Time: O(n); Space: O(1)
def is_palindrome3(my_string):
    string_length = len(my_string)
    middle_index = string_length // 2
    for index in range(middle_index):
        opposite_character_index = string_length - index - 1
        if my_string[index] != my_string[opposite_character_index]:
            return False
    return True
