from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# BFS; Time: O(n); Space: O(n)
def level_order_bfs(root):
    if not root:
        return []

    queue = deque([root])
    res = [[root.val]]

    while queue:
        level = []

        for i in range(len(queue)):
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
                level.append(current.left.val)
            if current.right:
                queue.append(current.right)
                level.append(current.right.val)

        if level:
            res.append(level)

    return res


# Test cases:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(level_order_bfs(root))
