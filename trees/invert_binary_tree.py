class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.val)


def build_tree_from_list_bfs(sequence):
    forest = [TreeNode(x) for x in sequence]

    for index, node in enumerate(forest):
        left_index = 2 * index + 1
        if left_index < len(forest):
            node.left = forest[left_index]

        right_index = 2 * index + 2
        if right_index < len(forest):
            node.right = forest[right_index]

    return forest[0]  # root


def invert_tree(root):
    if not root:
        return []

    root = build_tree_from_list_bfs(root)
    queue = [root]
    arr = []

    while queue:
        current = queue.pop(0)

        if current:
            arr.append(current.val)
            current.left, current.right = current.right, current.left

            queue.append(current.left)
            queue.append(current.right)

    return arr


print(invert_tree([4, 2, 7, 1, 3, 6, 9]) == [4, 7, 2, 9, 6, 3, 1])
print(invert_tree([2, 1, 3]) == [2, 3, 1])
print(invert_tree([]) == [])
