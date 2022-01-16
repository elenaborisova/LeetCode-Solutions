def roman_to_int(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900,
    }

    res = 0
    i = 0

    while i < len(s) - 1:
        pair = s[i] + s[i + 1]
        if pair in roman_map:
            res += int(roman_map[pair])
            i += 2
        else:
            res += int(roman_map[s[i]])
            i += 1

    if i < len(s):
        res += int(roman_map[s[i]])

    return res


# Test cases:
print(roman_to_int('MCDLXXVI'))
