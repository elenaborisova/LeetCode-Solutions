def count_students(students, sandwiches):
    students = students
    sandwiches = sandwiches
    unable_to_eat = 0

    while students:
        if not students[0] == sandwiches[0]:
            if all([s == 0 for s in students]) or all([s == 1 for s in students]):
                unable_to_eat = len(students)
                break
            students.append(students.pop(0))
        else:
            students.pop(0)
            sandwiches.pop(0)

    return unable_to_eat


print(count_students([1, 1, 0, 0], [0, 1, 0, 1]))
print(count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))
