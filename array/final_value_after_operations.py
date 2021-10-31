def find_final_value_after_operations(operations):
    value = 0

    for op in operations:
        if '-' in op:
            value -=1
        else:
            value += 1

    return value


print(find_final_value_after_operations(["--X", "X++", "X++"]))
print(find_final_value_after_operations(["++X", "++X", "X++"]))
print(find_final_value_after_operations(["X++", "++X", "--X", "X--"]))
