from ds_algorithms.trees.tree import TreeNode


# Time: O(n); Space: O(n)
def dfs(root, target, path=()):
    path = path + (root,)

    if root.value == target:
        return path

    for child in root.children:
        path_found = dfs(child, target, path)

        if path_found is not None:
            return path_found

    return None


sample_root_node = TreeNode("A")
b = TreeNode("B")
c = TreeNode("C")
sample_root_node.children = [b, c]
d = TreeNode("D")
e = TreeNode("E")
f = TreeNode("F")
g = TreeNode("G")
b.children = [d, e]
c.children = [f, g]

goal_path = dfs(sample_root_node, "F")
print(goal_path)
