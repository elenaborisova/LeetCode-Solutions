def decode(encoded, first):
    decoded = [0 for _ in range(len(encoded) + 1)]
    decoded[0] = first

    for i in range(len(encoded)):
        decoded[i + 1] = encoded[i] ^ decoded[i]

    return decoded


print(decode([1, 2, 3], 1))
print(decode([6, 2, 7, 3], 4))
