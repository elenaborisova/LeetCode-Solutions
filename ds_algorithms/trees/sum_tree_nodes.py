from collections import deque

from ds_algorithms.trees.tree import TreeNode


def sum_nodes_bfs(root):
    nodes_sum = 0
    queue = deque([root])

    while queue:
        current_node = queue.popleft()
        nodes_sum += current_node.value

        for child in current_node.children:
            queue.append(child)

    return nodes_sum


def sum_nodes_dfs(root):
    nodes_sum = 0
    if not root:
        return 0

    for child in root.children:
        nodes_sum += sum_nodes_dfs(child)

    return nodes_sum + root.value


sample_root_node = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
sample_root_node.children = [b, c]
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
b.children = [d, e]
c.children = [f, g]

nodes_sum = sum_nodes_bfs(sample_root_node)
print(nodes_sum)
