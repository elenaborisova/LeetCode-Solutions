class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


def has_cycle(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False


# Test cases:
def create_ll(nodes, pos):
    head = ListNode(nodes[0])
    prev = head

    if pos == 0:
        connection = head
    else:
        connection = None

    for i in range(1, len(nodes)):
        current = ListNode(nodes[i])
        prev.next = current
        prev = current

        if i == pos:
            connection = current

    prev.next = connection
    return head


head = create_ll(nodes=[3, 2, 0, -4], pos=1)
print(has_cycle(head) == True)

head_1 = create_ll(nodes=[1, 2], pos=0)
print(has_cycle(head_1) == True)

head_2 = create_ll(nodes=[1], pos=-1)
print(has_cycle(head_2) == False)
