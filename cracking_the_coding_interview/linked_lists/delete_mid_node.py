# Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
# the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
# that node.


def delete_mid_node(node):
    if node is None or node.get_next_mode() is None:
        return False

    node.value = node.get_next_mode().get_value()
    node.set_next_mode(node.get_next_mode().get_next_mode())
    return True
