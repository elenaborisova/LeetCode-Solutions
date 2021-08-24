def build_array(target, n):
    nums = []
    stack_operations = []

    for i in range(1, n + 1):
        stack_operations.append('Push')
        nums.append(i)
        if i not in target:
            stack_operations.append('Pop')
            nums.pop()

        if nums == target:
            return stack_operations


print(build_array([1, 2, 3], 3))
print(build_array([1, 2], 4))
print(build_array([2, 3, 4], 4))
print(build_array([1, 3], 3))
