class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def is_palindrome(head):
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Even/odd n nodes (will work without this step as well)
    head2 = slow
    if fast:
        head2 = head2.next

    # Reverse second half
    prev, cur = None, head2
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    head2 = prev

    # Check for palindrome
    one, two = head, head2
    while one and two:
        if one.val != two.val:
            return False
        one = one.next
        two = two.next
    return True


# Time: O(n); Space: O(1)
def is_palindrome2(head):
    # Find middle node
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    node = None
    while slow:
        next_node = slow.next
        slow.next = node
        node = slow
        slow = next_node

    # Check if the first half is the same as the second half
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


# Time: O(n); Space: O(n)
def is_palindrome3(head):
    stack = []  # storing first half

    # finding middle node
    slow = fast = head
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next

    if fast:  # when odd length
        slow = slow.next

    # compare both halves
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True


# Test cases:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next = ListNode(1)
print(is_palindrome2(head) == True)
