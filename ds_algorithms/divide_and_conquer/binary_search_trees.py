class BinarySearchTree:
    def __init__(self, value, depth=1):
        self.value = value
        self.depth = depth
        self.left = None
        self.right = None

    def insert(self, value):
        # Time: O(n) if imbalanced; O(log n) if balanced
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the left of {self.value} at depth {self.depth + 1}')
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value, self.depth + 1)
                print(f'Tree node {value} added to the right of {self.value} at depth {self.depth + 1}')
            else:
                self.right.insert(value)

    def get_node_by_value(self, value):
        # Time: O(n) if imbalanced; O(log n) if balanced
        if self.value == value:
            return self
        elif self.left is not None and value < self.value:
            return self.left.get_node_by_value(value)
        elif self.right is not None and value >= self.value:
            return self.right.get_node_by_value(value)
        else:
            return None

    # Traversals Time: O(n)
    def depth_first_traversal_inorder(self):  # left, root, right
        if self.left is not None:
            self.left.depth_first_traversal_inorder()
        print(f'Depth={self.depth}, Value={self.value}')
        if self.right is not None:
            self.right.depth_first_traversal_inorder()

    def depth_first_traversal_preorder(self):  # root, left, right
        print(f'Depth={self.depth}, Value={self.value}')
        if self.left is not None:
            self.left.depth_first_traversal_preorder()
        if self.right is not None:
            self.right.depth_first_traversal_preorder()

    def depth_first_traversal_postorder(self):  # left, right, root
        if self.left is not None:
            self.left.depth_first_traversal_postorder()
        if self.right is not None:
            self.right.depth_first_traversal_postorder()
        print(f'Depth={self.depth}, Value={self.value}')


root = BinarySearchTree(100)
root.insert(50)
root.insert(25)
root.insert(75)
root.insert(150)
root.insert(125)
root.insert(175)

print("Printing the inorder depth-first traversal:")
root.depth_first_traversal_inorder()

print("Printing the preorder depth-first traversal:")
root.depth_first_traversal_preorder()

print("Printing the postorder depth-first traversal:")
root.depth_first_traversal_postorder()
