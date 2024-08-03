"""141. Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/
Difficulty: Easy
Description: Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer."""

from package.data_structures import ListNode


class Solution:
    @staticmethod
    def hasCycle(head: ListNode) -> bool:
        """Optimal Solution: Floyd's Tortoise and Hare (Cycle Detection) Algorithm
           Time Complexity: O(n), Space Complexity: O(1)"""
        # Initialize two pointers: slow and fast
        slow, fast = head, head

        # Temporarily enable single value check for cycle detection
        ListNode.identity_check = True

        # Traverse the linked list
        while fast and fast.next:  # make sure fast.next also exists as we shift fast by two nodes
            # Move slow pointer by one node
            slow = slow.next
            # Move fast pointer by two nodes
            fast = fast.next.next
            # If there is a cycle, the slow and fast pointers will meet
            if slow == fast:
                return True

        # Disable single value check after cycle detection
        ListNode.identity_check = False
        return False


# Unit Test: Input: head = [3,2,0,-4], pos = 1, Output: True
# There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
head1 = ListNode.build_linked_list([3, 2, 0, -4])
head1.next.next.next.next = head1.next  # Connect the tail to the 1st node
assert Solution.hasCycle(head1) == True

# Unit Test: Input: head = [1,2], pos = 0, Output: True
# There is a cycle in the linked list, where the tail connects to the 0th node (0-indexed).
head2 = ListNode.build_linked_list([1, 2])
head2.next.next = head2  # Connect the tail to the 0th node
assert Solution.hasCycle(head2) == True

# Unit Test: Input: head = [1], pos = -1, Output: False
# There is no cycle in the linked list.
head3 = ListNode.build_linked_list([1])
assert Solution.hasCycle(head3) == False

print("All unit tests are passed")
