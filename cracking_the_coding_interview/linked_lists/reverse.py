from ds_algorithms.linked_list.linked_list import LinkedList


def reverse(ll):
    current_node = ll.get_head_node().get_next_node()
    prev_node = ll.get_head_node()

    while current_node:
        next_node = current_node.get_next_node()
        current_node.set_next_node(ll.get_head_node())
        prev_node.set_next_node(next_node)
        ll.head_node = current_node
        current_node = next_node

    return ll


def reverse2(ll):
    prev = None
    current = ll.get_head_node()

    while current:
        next = current.get_next_node()
        current.set_next_node(prev)
        prev = current
        current = next

    ll.head_node = prev


ll = LinkedList()
ll.insert_beginning('e')
ll.insert_beginning('d')
ll.insert_beginning('c')
ll.insert_beginning('b')
ll.insert_beginning('a')

print(ll.stringify_list())
reverse2(ll)
print(ll.stringify_list())


# Time: O(n)
# Space: O(1)
