from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# DFS; Time: O(n); Space: O(n)
def max_depth_dfs(root):
    if not root:
        return 0

    left = max_depth_dfs(root.left)
    right = max_depth_dfs(root.right)

    return max(left, right) + 1


# DFS; Time: O(n); Space: O(n)
def max_depth_dfs2(root, depth=0):
    if not root:
        return depth

    left = max_depth_dfs2(root.left, depth + 1)
    right = max_depth_dfs2(root.right, depth + 1)

    return max(left, right)


# DFS; Iterative using stack
def max_depth_dfs3(root):
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])

    return res


# BFS; Time: O(n); Space: O(n)
def max_depth_bfs(root):
    if not root:
        return 0

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


def max_depth_bfs2(root):
    if root is None:
        return 0

    queue = deque([root])
    level = 0

    while queue:
        for i in range(len(queue)):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        level += 1

    return level


# Test cases:
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root2 = TreeNode(1)
root2.right = TreeNode(2)

root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.left.left = TreeNode(4)
root3.right = TreeNode(3)
root3.right.right = TreeNode(5)

print(max_depth_dfs3(root))
