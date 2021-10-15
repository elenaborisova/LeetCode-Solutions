def array_rank_transform(arr):
    sorted_elements = sorted(set(arr))
    el_ranks = {}

    for i, el in enumerate(sorted_elements):
        if el not in el_ranks:
            el_ranks[el] = i + 1

    ranks = [el_ranks[el] for el in arr]
    return ranks


print(array_rank_transform([40, 10, 20, 30]))
print(array_rank_transform([100, 100, 100]))
print(array_rank_transform([37, 12, 28, 9, 100, 56, 80, 5, 12]))
print(array_rank_transform([-5, 6, 5, -44, 27, 14, -27, 36, -17, -6, 13, -12]))
