# Brute Force; Time: O(n ^ 3)
def print_solution():
    n = 1000

    for a in range(1, n):
        for b in range(1, n):
            for c in range(1, n):
                d = pow(a ** 3 + b ** 3 - c ** 3, 1/3)
                d = int(d)
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    print(a, b, c, d)


# Mapping; Time: O(n ^ 2)
def print_solution1():
    n = 1000
    mapping = {}

    for c in range(1, n):
        for d in range(1, n):
            result = c ** 3 + d ** 3
            if result not in mapping:
                mapping[result] = []
            mapping[result].append((c, d))

    for result, map in mapping.items():
        for pair1 in map:
            for pair2 in map:
                print(*pair1, *pair2)


print_solution1()
