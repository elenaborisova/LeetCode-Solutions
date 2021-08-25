def min_deletion_size(strs):
    min_size = 0

    for i in range(len(strs[0])):
        current = []
        for j in range(len(strs)):
            current.append(strs[j][i])

        if not current == sorted(current):
            min_size += 1

    return min_size


print(min_deletion_size(["cba", "daf", "ghi"]))
print(min_deletion_size(["a", "b"]))
print(min_deletion_size(["zyx", "wvu", "tsr"]))
