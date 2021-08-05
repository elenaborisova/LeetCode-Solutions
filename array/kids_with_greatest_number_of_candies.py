def kids_with_candies(candies, extra_candies):
    result = []

    for i in range(len(candies)):
        is_greater = all(candies[i] + extra_candies >= x for x in candies)
        result.append(is_greater)

    return result


print(kids_with_candies([2, 3, 5, 1, 3], 3))
print(kids_with_candies([4, 2, 1, 1, 2], 1))
