class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def is_valid_bst(root, left=float('-inf'), right=float('inf')):
    if not root:
        return True

    if not (right > root.val > left):
        return False

    return is_valid_bst(root.left, left, root.val) and is_valid_bst(root.right, root.val, right)


# Test cases:
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(5)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(6)

print(is_valid_bst(root))
