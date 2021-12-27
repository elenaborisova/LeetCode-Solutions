from collections import deque


class Node:
    def __init__(self, data):
        self.val = data
        self.children = []


def count_of_nodes(root, queries, s):
    letters_map = {i: c for i, c in enumerate(s, start=1)}
    result = []

    for query in queries:
        node_val, letter = query

        queue = deque([root])
        visited = []
        new_root_is_found = False

        while queue:
            current = queue.popleft()

            if not new_root_is_found and current.val == node_val:
                new_root_is_found = True
                queue = deque([current])
                continue

            for child in current.children:
                queue.append(child)

            if new_root_is_found and current.val == letter:
                visited.append(current)

        count = len([n for n in visited if letters_map[n.val] == letter])
        result.append(count)

    return result


# Testcase 1
s_1 = 'aba'
root_1 = Node(1)
root_1.children.append(Node(2))
root_1.children.append(Node(3))
queries_1 = [(1, 'a')]
expected_1 = [2]
print(count_of_nodes(root_1, queries_1, s_1) == expected_1)


# Testcase 2
s_2 = 'abaacab'
root_2 = Node(1)
root_2.children.append(Node(2))
root_2.children.append(Node(3))
root_2.children.append(Node(7))
root_2.children[0].children.append(Node(4))
root_2.children[0].children.append(Node(5))
root_2.children[1].children.append(Node(6))
queries_2 = [(1, 'a'), (2, 'b'), (3, 'a')]
expected_2 = [4, 1, 2]
print(count_of_nodes(root_2, queries_2, s_2) == expected_2)

