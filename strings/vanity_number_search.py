def get_vanity_number(code):
    decoded = ''
    vanity_map = {
        'A': '2',
        'B': '22',
        'C': '222',
        'D': '3',
        'E': '33',
        'F': '333',
        'G': '4',
        'H': '44',
        'I': '444',
        'J': '5',
        'K': '55',
        'L': '555',
        'M': '6',
        'N': '66',
        'O': '666',
        'P': '7',
        'Q': '77',
        'R': '777',
        'S': '7777',
        'T': '8',
        'U': '88',
        'V': '888',
        'W': '9',
        'X': '99',
        'Y': '999',
        'Z': '9999'
    }

    for char in code:
        decoded += vanity_map[char]

    return decoded


def search_vanity_number(codes, numbers):
    res = []

    for code in codes:
        decoded = get_vanity_number(code)
        for num in numbers:
            if decoded in num:
                res.append(num)

    return sorted(res)


def get_user_input():
    codes = []
    numbers = []

    c = int(input())
    for _ in range(c):
        code = input()
        codes.append(code)

    n = int(input())
    for _ in range(n):
        number = input()
        numbers.append(number)

    return codes, numbers


codes, numbers = get_user_input()
print(search_vanity_number(codes, numbers))
