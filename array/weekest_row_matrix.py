def k_weakest_rows(mat, k):
    soldiers_count = {}
    indices = []

    for i in range(len(mat)):
        soldiers_count[i] = mat[i].count(1)

    soldiers_count = dict(sorted(soldiers_count.items(), key=lambda x: (x[1], x[0])))

    for row in soldiers_count.keys():
        if len(indices) == k:
            break

        indices.append(row)

    return indices


print(k_weakest_rows(mat=
                     [[1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 0],
                      [1, 0, 0, 0, 0],
                      [1, 1, 0, 0, 0],
                      [1, 1, 1, 1, 1]],
                     k=3))

print(k_weakest_rows(mat=
                     [[1, 0, 0, 0],
                      [1, 1, 1, 1],
                      [1, 0, 0, 0],
                      [1, 0, 0, 0]],
                     k=2))