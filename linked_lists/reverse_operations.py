class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def get_list_repr(head):
    result = []
    curr = head
    while curr:
        result.append(curr.value)
        curr = curr.next

    return result


def reverse(head: Node):
    prev_node = head
    current_node = head.next
    next_node = current_node.next

    if head.value % 2 == 0:
        change_head = True
    else:
        change_head = False

    while current_node.next:
        if change_head and current_node.value % 2 == 0:
            current_node.next = head
            prev_node.next = next_node
            head = current_node
            current_node = next_node

        elif not change_head and current_node.value % 2 == 0:
            current_node.next = next_node.next
            prev_node.next = next_node
            next_node.next = current_node

            prev_node = current_node
            if current_node.next:
                current_node = current_node.next

        else:
            change_head = False
            prev_node = current_node
            current_node = next_node

        if current_node.next:
            next_node = current_node.next

    return get_list_repr(head)


lst = [1, 2, 8, 9, 12, 16]
head = Node(1)
lst2 = [2, 18, 24, 26, 3, 5, 7, 9, 6, 12, 1]
head2 = Node(2)

for val in lst2[1:]:
    new_node = Node(val)
    last = head2
    while last.next:
        last = last.next
    last.next = new_node

print(reverse(head2))
