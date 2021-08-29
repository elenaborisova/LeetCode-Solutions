def find_words(words):
    valid_words = []
    rows = {
        'first': 'qwertyuiop',
        'second': 'asdfghjkl',
        'third': 'zxcvbnm',
    }

    for i in range(len(words)):
        if all([l in rows['first'] for l in words[i].lower()]):
            valid_words.append(words[i])
        elif all([l in rows['second'] for l in words[i].lower()]):
            valid_words.append(words[i])
        elif all([l in rows['third'] for l in words[i].lower()]):
            valid_words.append(words[i])

    return valid_words


print(find_words(["Hello", "Alaska", "Dad", "Peace"]))
print(find_words(["omk"]))
print(find_words(["adsdf", "sfd"]))
print(find_words(["a", "b"]))
