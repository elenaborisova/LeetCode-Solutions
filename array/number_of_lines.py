def number_of_lines(widths, s):
    lines_count = 0
    pixels_count = 0

    for i in range(len(s)):
        l_ord = ord(s[i]) - 97
        pixels = widths[l_ord]

        if pixels_count + pixels <= 100:
            pixels_count += pixels
        else:
            lines_count += 1
            pixels_count = pixels

    lines_count += 1

    return [lines_count, pixels_count]


print(number_of_lines(
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    "abcdefghijklmnopqrstuvwxyz"))
print(number_of_lines(
    widths=[4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    s="bbbcccdddaaa"))