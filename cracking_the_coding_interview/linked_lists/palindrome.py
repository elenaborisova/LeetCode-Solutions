from ds_algorithms.linked_list.linked_list import LinkedList


def is_palindrome(node):
    reversed_ll = LinkedList()
    slow_pointer = node
    fast_pointer = node

    while fast_pointer and fast_pointer.get_next_node():
        fast_pointer = fast_pointer.get_next_node()
        reversed_ll.insert_beginning(slow_pointer.get_value())
        if fast_pointer.get_next_node():
            slow_pointer = slow_pointer.get_next_node()
            fast_pointer = fast_pointer.get_next_node()

    if not fast_pointer:
        slow_pointer = slow_pointer.get_next_node()
    reversed_node = reversed_ll.get_head_node()

    while slow_pointer:
        if not slow_pointer.get_value() == reversed_node.get_value():
            return False

        slow_pointer = slow_pointer.get_next_node()
        reversed_node = reversed_node.get_next_node()

    return True


ll = LinkedList()
ll.insert_beginning('a')
ll.insert_beginning('b')
ll.insert_beginning('c')
ll.insert_beginning('c')
ll.insert_beginning('b')
ll.insert_beginning('a')

print(is_palindrome(ll.get_head_node()))
