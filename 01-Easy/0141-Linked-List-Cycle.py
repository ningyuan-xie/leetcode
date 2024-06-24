# Link: https://leetcode.com/problems/linked-list-cycle/
# Difficulty: Easy
# Description: Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be
# reached again by continuously following the next pointer.

from typing import List
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def hasCycle(head: ListNode) -> bool:
        # Initialize two pointers: slow and fast
        slow = fast = head
        # Traverse the linked list
        while fast and fast.next:
            # Move slow pointer by one node
            slow = slow.next
            # Move fast pointer by two nodes
            fast = fast.next.next
            # Check if the slow and fast pointers meet
            if slow == fast:
                return True
        return False


# Unit Test: Input: head = [3,2,0,-4], pos = 1, Output: True
head1 = ListNode(3, ListNode(2, ListNode(0, ListNode(-4))))
head1.next.next.next.next = head1.next
assert Solution.hasCycle(head1) == True

# Unit Test: Input: head = [1,2], pos = 0, Output: True
head2 = ListNode(1, ListNode(2))
head2.next.next = head2
assert Solution.hasCycle(head2) == True

# Unit Test: Input: head = [1], pos = -1, Output: False
head3 = ListNode(1)
assert Solution.hasCycle(head3) == False

print("All unit tests are passed")
