def rotate_char(char, rotation_factor, upper_bound, lower_bound, count):
    char_ord = ord(char)

    while char_ord not in range(lower_bound, upper_bound + 1):
        char_ord = ((char_ord - lower_bound + rotation_factor) % count) + lower_bound
    else:
        char_ord += rotation_factor

    return char_ord


def rotational_cipher(s, rotation_factor):
    new_s = ''

    for char in s:
        if char.isalpha() and char.isupper():
            char_ord = rotate_char(char, rotation_factor, 90, 65, 26)
            new_s += chr(char_ord)
        elif char.isalpha() and char.islower():
            char_ord = rotate_char(char, rotation_factor, 122, 97, 26)
            new_s += chr(char_ord)
        elif char.isdigit():
            char_ord = rotate_char(char, rotation_factor, 57, 48, 10)
            new_s += chr(char_ord)
        else:
            new_s += char

    return new_s


print(rotational_cipher('abcdefghijklmNOPQRSTUVWXYZ0123456789', 39))
print(rotational_cipher("Nyx'd mbi, czkxscr pvkdwkdo", 1232))
