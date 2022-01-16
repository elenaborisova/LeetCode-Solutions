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


def arrange_names(names):
    int_to_roman = {}

    for i, name_r in enumerate(names):
        name, r_num = name_r.split()
        num = roman_to_int(r_num)
        int_to_roman[num] = r_num
        names[i] = (name, num)

    names.sort()

    for i, name_num in enumerate(names):
        name, num = name_num
        r_num = int_to_roman[num]
        names[i] = f'{name} {r_num}'

    return names


# Test cases:
names = ['z I', 'zz X', 'Louis V', 'Louis VI', 'Louis X', 'Peter I']
print(arrange_names(names))
