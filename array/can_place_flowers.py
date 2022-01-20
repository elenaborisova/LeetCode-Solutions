def can_place_flowers(flowerbed, n):
    i = 0

    while i < len(flowerbed):
        if flowerbed[i] == 0 \
                and (i == 0 or flowerbed[i - 1] == 0) \
                and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
        i += 1

        if n <= 0:
            return True

    return False


# Test cases:
print(can_place_flowers([1, 0, 0, 0, 1], 1) == True)
print(can_place_flowers([1, 0, 0, 0, 1], 2) == False)
print(can_place_flowers([0, 0, 1, 0, 1], 1) == True)
print(can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2) == True)
print(can_place_flowers([0], 1) == True)
print(can_place_flowers([0, 0, 0, 0, 0, 1, 0, 0], 0) == True)
