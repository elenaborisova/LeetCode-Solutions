def count_good_rectangles(rectangles):
    lengths = []

    for rect in rectangles:
        l = rect[0]
        w = rect[1]
        max_length = min(l, w)
        lengths.append(max_length)

    return lengths.count(max(lengths))


print(count_good_rectangles([[5, 8], [3, 9], [5, 12], [16, 5]]))
print(count_good_rectangles([[2, 3], [3, 7], [4, 3], [3, 7]]))
