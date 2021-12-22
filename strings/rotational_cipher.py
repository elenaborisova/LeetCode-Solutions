def rotate_char(char_ord, upper_bound, lower_bound):

    while char_ord not in range(lower_bound, upper_bound + 1):
        overhead = char_ord - upper_bound
        char_ord = (lower_bound - 1) + overhead

    return char_ord


def rotational_cipher(s, rotation_factor):
    new_s = ''

    for char in s:
        if char.isalpha() and char.isupper():
            char_ord = rotate_char(ord(char) + rotation_factor, 90, 65)
            new_s += chr(char_ord)
        elif char.isalpha() and char.islower():
            char_ord = rotate_char(ord(char) + rotation_factor, 122, 97)
            new_s += chr(char_ord)
        elif char.isdigit():
            char_ord = rotate_char(ord(char) + rotation_factor, 57, 48)
            new_s += chr(char_ord)
        else:
            new_s += char

    return new_s


print(rotational_cipher('abcdefghijklmNOPQRSTUVWXYZ0123456789', 39))
