class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


# Time: O(n * m)
def is_subtree(root, subroot):
    if not subroot:
        return True
    if not root:
        return False

    if is_same_tree(root, subroot):
        return True

    return is_subtree(root.left, subroot) or is_subtree(root.right, subroot)


def is_same_tree(root, subroot):
    if not root and not subroot:
        return True

    if root and subroot and root.val == subroot.val:
        return is_subtree(root.left, subroot.left) and is_subtree(root.right, subroot.right)


# Test cases:
root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(0)

subroot = TreeNode(4)
subroot.left = TreeNode(1)
subroot.right = TreeNode(2)

root2 = TreeNode(1)
root2.left = TreeNode(1)
subroot2 = TreeNode(1)

print(is_subtree(root2, subroot2))
