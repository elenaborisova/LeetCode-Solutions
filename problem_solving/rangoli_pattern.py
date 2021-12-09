def print_rangoli(size):
    letters = []
    dash_count = size * 2 - 2

    # Upper part
    for i in range(1, size + 1):
        curr_letter = chr(97 + size - i)
        letters.append(curr_letter)

        print('-' * dash_count +
              '-'.join(letters[:-1] + letters[::-1]) +
              '-' * dash_count)

        dash_count -= 2

    # Lower part
    dash_count = 2
    for i in range(size - 1, 0, -1):
        letters.pop()
        print('-' * dash_count +
              '-'.join(letters[:-1] + letters[::-1]) +
              '-' * dash_count)

        dash_count += 2


print_rangoli(5)
