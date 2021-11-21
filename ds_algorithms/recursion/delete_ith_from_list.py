from ds_algorithms.linked_list.linked_list import LinkedList


def remove_node(head, i):
    if i < 0:
        return head
    if head is None:
        return None
    if i == 0:
        return head.next_node

    head.next_node = remove_node(head.next_node, i - 1)
    return head


gemstones = LinkedList()
gemstones.insert_beginning('Pearl')
gemstones.insert_beginning('Jade')
gemstones.insert_beginning('Sapphire')
gemstones.insert_beginning('Amber')
head = remove_node(gemstones.get_head_node(), 1)
