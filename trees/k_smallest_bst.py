import heapq
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# BFS and MaxHeap
def kth_smallest(root, k):
    h = []
    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current:
            heapq.heappush(h, current.val * -1)
            queue.append(current.left)
            queue.append(current.right)

        if len(h) > k:
            heapq.heappop(h)

    return h[0] * -1


# InOrder recursive
def kth_smallest2(root, k):
    return inorder(root)[k - 1]


def inorder(root):
    if not root:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)


# InOrder recursive
def kth_smallest3(root, k):
    position = 0
    return kth_smallest_rec(root, k, position)


def kth_smallest_rec(root, k, position):
    if not root:
        return root

    left = kth_smallest_rec(root.left, k, position)
    if left:
        return left

    position += 1
    if position == k:
        return root

    return kth_smallest_rec(root.right, k, position)


# InOrder with Stack (iterative)
def kth_smallest4(root, k):
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        k -= 1

        if not k:
            return root.val

        root = root.right


# Test cases:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)


root2 = TreeNode(3)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.left.right = TreeNode(2)

print(kth_smallest3(root, 6))
