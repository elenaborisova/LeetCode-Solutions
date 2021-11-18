# Recursive approach - Time: O(n); Space: O(n)
def find_min(my_list):
    if not my_list:
        return None

    if len(my_list) == 1:
        return my_list[0]

    min_el = min(my_list[0], find_min(my_list[1:]))
    return min_el


# Iterative approach - Time: O(n); Space: O(1)
def find_min2(my_list):
    min_el = None
    for element in my_list:
        if not min_el or (element < min_el):
            min_el = element
    return min_el


print(find_min([42, 17, 2, -1, 67]) == -1)
print(find_min([]) is None)
print(find_min([13, 72, 19, 5, 86]) == 5)
