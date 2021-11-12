# Create a method that returns the middle node of a linked list.

def find_middle(linked_list):
    fast = linked_list.head_node
    slow = linked_list.head_node

    while fast:
        fast = fast.get_next_node()
        if fast:
            fast = fast.get_next_node()
            slow = slow.get_next_node()

    return slow


# Time: O(n)
# Space: O(1)
