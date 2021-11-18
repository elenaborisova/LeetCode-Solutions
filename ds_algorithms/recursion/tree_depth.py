# Iterative approach - Time: O(n); Space: O(n)
def depth2(tree):
    result = 0
    queue = [tree]

    while queue:
        level_count = len(queue)
        for child_count in range(0, level_count):
            child = queue.pop(0)

            if child.get("left_child"):
                queue.append(child["left_child"])
            if child.get("right_child"):
                queue.append(child["right_child"])

        result += 1
    return result


# Recursive approach - Time: O(n) *n is the number of nodes; Space: O(h) *h is the height of the tree
def depth(tree_node):
    if tree_node is None:
        return 0

    left_depth = depth(tree_node['left_child'])
    right_depth = depth(tree_node['right_child'])

    if left_depth > right_depth:
        return left_depth + 1
    return right_depth + 1


# HELPER FUNCTION TO BUILD TREES
def build_bst(my_list):
    if len(my_list) == 0:
        return None

    mid_idx = len(my_list) // 2
    mid_val = my_list[mid_idx]

    tree_node = {"data": mid_val}
    tree_node["left_child"] = build_bst(my_list[: mid_idx])
    tree_node["right_child"] = build_bst(my_list[mid_idx + 1:])

    return tree_node


tree_level_1 = build_bst([1])
tree_level_2 = build_bst([1, 2, 3])
tree_level_4 = build_bst([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])


print(depth(tree_level_1) == 1)
print(depth(tree_level_2) == 2)
print(depth(tree_level_4) == 4)
