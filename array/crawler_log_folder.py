def min_operations(logs):
    count = 0

    for log in logs:
        if log == '../':
            count = max(0, count - 1)
        elif not log == './':
            count += 1

    return count


print(min_operations(["d1/", "d2/", "../", "d21/", "./"]))
print(min_operations(["d1/", "d2/", "./", "d3/", "../", "d31/"]))
print(min_operations(["d1/", "../", "../", "../"]))
print(min_operations(["./", "wz4/", "../", "mj2/", "../", "../", "ik0/", "il7/"]))
print(min_operations(["./", "../", "./"]))
