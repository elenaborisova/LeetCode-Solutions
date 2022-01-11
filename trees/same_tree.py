from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# BFS; Time: O(n); Space: O(n)
def is_same_tree_bfs(p, q):
    p_queue = deque([p])
    q_queue = deque([q])

    while p_queue and q_queue:
        p_node = p_queue.popleft()
        q_node = q_queue.popleft()

        if p_node is None and q_node is None:
            continue

        if (p_node is None and q_node) \
                or (q_node is None and p_node) \
                or (p_node.val != q_node.val):
            return False

        p_queue.append(p_node.left)
        p_queue.append(p_node.right)

        q_queue.append(q_node.left)
        q_queue.append(q_node.right)

    return True


# DFS; Time: O(n); Space: O(n)
def is_same_tree_dfs(p, q):
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val != q.val:
        return False

    left_nodes = is_same_tree_dfs(p.left, q.left)
    right_nodes = is_same_tree_dfs(p.right, q.right)

    return left_nodes and right_nodes


# Test cases:
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)

root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

print(is_same_tree_dfs(root1, root2))
