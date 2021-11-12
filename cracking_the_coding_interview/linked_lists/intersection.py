from ds_algorithms.linked_list.linked_list import LinkedList


def get_size_and_tails(ll1, ll2):
    current1 = ll1.get_head_node()
    count1 = 1
    while current1.get_next_node():
        count1 += 1
        current1 = current1.get_next_node()
    tail1 = current1

    current2 = ll2.get_head_node()
    count2 = 1
    while current2.get_next_node():
        count2 += 1
        current2.get_next_node()
    tail2 = current2

    return count1, count2, tail1, tail2


def intersection(ll1, ll2):
    size1, size2, tail1, tail2 = get_size_and_tails(ll1, ll2)
    if not tail1 == tail2:
        return False

    longer = ll1.get_head_node() if size1 > size2 else ll2.get_head_node()
    shorter = ll1.get_head_node() if size1 < size2 else ll2.get_head_node()
    size_diff = longer - shorter

    while longer and size_diff > 0:
        longer = longer.get_next_node()
        size_diff -= 1

    while not longer == shorter:
        longer = longer.get_next_node()
        shorter = shorter.get_next_node()

    return longer

