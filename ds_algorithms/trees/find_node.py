from collections import deque

from ds_algorithms.trees.tree import TreeNode


def find_node_dfs(root, target):
    if root.value == target:
        return root

    for child in root.children:
        node_found = find_node_dfs(child, target)

        if node_found:
            return node_found

    return None


def find_node_bfs(root, target):
    queue = deque([root])

    while queue:
        current_node = queue.popleft()

        if current_node.value == target:
            return current_node

        for child in current_node.children:
            queue.append(child)

    return None


sample_root_node = TreeNode("Home")
docs = TreeNode("Documents")
photos = TreeNode("Photos")
sample_root_node.children = [docs, photos]
my_wish = TreeNode("WishList.txt")
my_todo = TreeNode("TodoList.txt")
my_cat = TreeNode("Fluffy.jpg")
my_dog = TreeNode("Spot.jpg")
docs.children = [my_wish, my_todo]
photos.children = [my_cat, my_dog]


node_found = find_node_dfs(sample_root_node, "Fluffy.jpg")
print(node_found)
