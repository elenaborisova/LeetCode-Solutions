class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def build_tree(preorder, inorder):
    if len(inorder) == 0:
        return None

    root = TreeNode(preorder.pop(0))

    left = build_tree(preorder, inorder[:inorder.index(root.val)])
    right = build_tree(preorder, inorder[inorder.index(root.val) + 1:])

    root.left = left
    root.right = right

    return root


print(build_tree([3, 9, 20, 1, 15, 7], [1, 9, 3, 15, 20, 7]))

