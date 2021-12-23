class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        
    def __repr__(self):
        return str(self.data)


def reverse_sublist(head):
    prev_node = None
    current_node = head

    while current_node and current_node.data % 2 == 0:
        next_node = current_node.next
        current_node.next = prev_node
        prev_node = current_node
        current_node = next_node

    if not current_node:
        next_part = None
    else:
        next_part = current_node

    return prev_node, next_part


def reverse(head):
    current_node = head
    prev_node = dummy = Node("dummy")
    dummy.next = head
    
    while current_node:
        if current_node.data % 2 != 0:
            prev_node = current_node
            current_node = current_node.next
        else:
            new_head, next_part = reverse_sublist(current_node)
            prev_node.next = new_head
            current_node.next = next_part
            current_node = current_node.next

    return dummy.next


lst = [1, 2, 8, 9, 12, 16]
head = Node(1)
lst2 = [2, 18, 24, 26, 3, 5, 7, 9, 6, 12, 1]
head2 = Node(2)

for val in lst2[1:]:
    new_current = Node(val)
    last = head2
    while last.next:
        last = last.next
    last.next = new_current

print(reverse(head2))
