# Recursive approach - Time: O(n); Space: O(n)
def multiplication(num_1, num_2):
    if num_2 <= 1:
        return num_1

    return num_1 + multiplication(num_1, num_2 - 1)


# Iterative approach - Time: O(n); Space: O(1)
def multiplication2(num_1, num_2):
    result = 0
    for count in range(0, num_2):
        result += num_1
    return result
