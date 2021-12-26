from collections import deque


class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def visible_nodes_dfs(root):
    if not root:
        return 0

    left_count = visible_nodes_dfs(root.left)
    right_count = visible_nodes_dfs(root.right)

    return max(left_count, right_count) + 1


def visible_nodes_bfs(root):
    queue = deque([root, None])
    depth = 0

    while queue:
        current = queue.popleft()

        if current is None:
            depth += 1

        if current:
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        elif queue:
            queue.append(None)

    return depth


def visible_nodes_bfs2(root):
    if not root:
        return 0

    queue = deque([root])
    left_visibles = []

    while queue:
        for i in range(len(queue)):
            current = queue.popleft()

            if i == 0:
                left_visibles.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    return len(left_visibles)


root_1 = TreeNode(8)
root_1.left = TreeNode(3)
root_1.right = TreeNode(10)
root_1.left.left = TreeNode(1)
root_1.left.right = TreeNode(6)
root_1.left.right.left = TreeNode(4)
root_1.left.right.right = TreeNode(7)
root_1.right.right = TreeNode(14)
root_1.right.right.left = TreeNode(13)
print(visible_nodes_dfs(root_1))

root_2 = TreeNode(10)
root_2.left = TreeNode(8)
root_2.right = TreeNode(15)
root_2.left.left = TreeNode(4)
root_2.left.left.right = TreeNode(5)
root_2.left.left.right.right = TreeNode(6)
root_2.right.left = TreeNode(14)
root_2.right.right = TreeNode(16)
print(visible_nodes_dfs(root_2))
