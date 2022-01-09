class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


# Creating a new linked list
def merge_two_lists(list1, list2):
    if not list1 and not list2:
        return None
    if not list1:
        return list2
    if not list2:
        return list1

    one, two = list1, list2

    if one.val <= two.val:
        head = one
        one = one.next
    else:
        head = two
        two = two.next
    current = head

    while one and two:
        if one.val <= two.val:
            current.next = one
            current = one
            one = current.next
        else:
            current.next = two
            current = two
            two = current.next

    current.next = one or two  # appends whatever is remaining

    return head


# Merging two linked lists; Iterative
def merge_two_lists3(l1, l2):
    dummy = cur = ListNode(0)

    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next

        cur = cur.next

    cur.next = l1 or l2

    return dummy.next


# recursive approach
def merge_two_lists2(a, b):
    if a and b:
        if a.val > b.val:
            a, b = b, a

        a.next = merge_two_lists2(a.next, b)

    return a or b


# Test cases:
head1 = ListNode(1)
head1.next = ListNode(2)
head1.next.next = ListNode(4)
head1.next.next.next = ListNode(8)

head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(7)

print(merge_two_lists(head1, head2))
