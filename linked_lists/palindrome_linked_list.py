class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)


def is_palindrome(head):
    # Time: O(n); Space: O(1)

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


def is_palindrome2(head):
    # Time: O(n); Space: O(n)

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
