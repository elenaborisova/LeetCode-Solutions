def decrypt(code, k):
    decoded = []

    if k > 0:
        for i in range(len(code)):
            num = 0
            idx = i
            count = 0
            while count < k:
                if idx == len(code):
                    idx = 0

                num += code[idx]
                idx += 1
                count += 1
            decoded.append(num)

        return decoded[1:] + decoded[:1]

    elif k < 0:
        for i in range(len(code)):
            num = 0
            idx = i
            count = 0
            while count < k * -1:
                if idx == -1:
                    idx = len(code) - 1

                num += code[idx]
                idx -= 1
                count += 1
            decoded.append(num)

        return decoded[-1:] + decoded[:-1]

    else:
        return [0 for _ in range(len(code))]


print(decrypt([5, 7, 1, 4], 3))
print(decrypt([1, 2, 3, 4], 0))
print(decrypt([2, 4, 9, 3], -2))
