# Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
# beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
# as to make a loop in the linked list.
from ds_algorithms.linked_list.linked_list import LinkedList


def find_loop_beginning(ll):
    fast = ll.get_head_node()
    slow = ll.get_head_node()

    # Find first collision point
    while fast.get_next_node() and slow.get_next_node():
        slow = slow.get_next_node()
        fast = fast.get_next_node().get_next_node()

        if slow == fast:
            break
    else:  # If not break; no collision point
        return

    slow = ll.get_head_node()
    while not slow == fast:
        slow = slow.get_next_node()
        fast = fast.get_next_node()

    return fast  # or slow
