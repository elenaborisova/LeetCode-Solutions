def unique_morse_representations(words):
    morse_table = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..'}

    unique_reprs = set()

    for word in words:
        current = ''
        for letter in word:
            current += morse_table[letter.upper()]
        unique_reprs.add(current)

    return len(unique_reprs)


print(unique_morse_representations(["gin", "zen", "gig", "msg"]))
print(unique_morse_representations(["a"]))
