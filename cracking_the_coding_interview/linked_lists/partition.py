# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.


from ds_algorithms.linked_list.linked_list import LinkedList


def partition(node, x):
    smaller = LinkedList()
    greater = LinkedList()

    while node.get_next_node():
        next_node = node.get_next_node()

        if node.get_value() < x:
            smaller.insert_beginning(node.get_value())
        else:
            greater.insert_beginning(node.get_value())

        node = next_node

    current = smaller.get_head_node()
    while current.get_next_node():
        greater.insert_beginning(current.get_value())
        current = current.get_next_node()

    print(greater.stringify_list())


ll = LinkedList()
ll.insert_beginning(1)
ll.insert_beginning(2)
ll.insert_beginning(10)
ll.insert_beginning(5)
ll.insert_beginning(8)
ll.insert_beginning(5)
ll.insert_beginning(3)

partition(ll.get_head_node(), 5)
