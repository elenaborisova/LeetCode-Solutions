def restore_string(s, indices):
    restored = ['None' for _ in range(len(s))]

    for i in range(len(indices)):
        restored[indices[i]] = s[i]

    return ''.join(restored)


print(restore_string('codeleet', [4, 5, 6, 7, 0, 2, 1, 3]))
print(restore_string('abc', [0, 1, 2]))
print(restore_string('aiohn', [3, 1, 4, 2, 0]))
print(restore_string('aaiougrt', [4, 0, 2, 6, 7, 3, 1, 5]))
print(restore_string('art', [1, 0, 2]))
