from collections import deque


def find_signature_counts(arr):
    signatures = [0] * len(arr)
    yearbooks = {student: deque([student]) for student in arr}

    while yearbooks:
        for i in range(len(arr)):
            from_student = arr[i]
            to_student = arr[from_student - 1]
            if from_student not in yearbooks:
                continue

            yearbook = yearbooks[from_student].popleft()
            signatures[arr.index(yearbook)] += 1

            if yearbook != to_student:
                yearbooks[to_student].append(yearbook)
            else:
                yearbooks.pop(from_student)

    return signatures


def find_signature_counts_optimized(arr):
    res = []

    for i, elem in enumerate(arr):
        value = elem
        count = 1

        while arr[value-1] != elem:
            value = arr[value - 1]
            count += 1
        res.append(count)

    return res


# Test cases:
print(find_signature_counts([1, 2]))
print(find_signature_counts([2, 1]))
print(find_signature_counts([5, 1, 2, 4, 3]))
print(find_signature_counts([4, 2, 3, 1]))
print(find_signature_counts([1, 2, 3, 4, 5, 6]))
