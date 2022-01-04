def answer_queries(queries, n):
    output = []
    true_indices = set()

    for q in queries:
        if q[0] == 1:  # set
            idx = q[1]
            true_indices.add(idx)
        elif q[0] == 2:  # get
            idx = q[1]
            for j in range(idx, n):
                if j in true_indices:
                    output.append(j)
                    break
            else:
                output.append(-1)

    return output


# Test cases:
print(answer_queries([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]], 5) == [-1, 2, -1, 2])
print(answer_queries([[2, 3], [1, 2], [2, 1], [2, 3], [2, 2], [1, 3], [2, 3], [2, 1]], 5) == [-1, 2, -1, 2, 3, 2])
print(answer_queries([[1, 2], [1, 4], [2, 1], [2, 2], [2, 3], [2, 4]], 5) == [2, 2, 4, 4])
