# remove duplicates from an unsorted linked list


def remove_duplicates(ll_node):
    # Time: O(n)
    # Space: O(n)
    ll_hash = []
    prev_node = None

    while ll_node:
        if ll_node.get_value() in ll_hash:
            prev_node.set_next_node(ll_node.get_next_node())
        else:
            ll_hash.append(ll_node.get_value())
            prev_node = ll_node

        ll_node = ll_node.get_next_node()


def remove_duplicates2(head):
    # Two pointers
    # Time: O(n^2)
    # Space: O(1)
    current = head

    while current:
        runner = current
        while runner.get_next_node() is not None:
            if runner.get_next_node().get_value() == current.get_value():
                runner.set_next_node(runner.get_next_node().get_next_node())
            else:
                runner = runner.get_next_node()

        current = current.get_next_node()
