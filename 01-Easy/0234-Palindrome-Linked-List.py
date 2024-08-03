"""234. Palindrome Linked List
Link: https://leetcode.com/problems/palindrome-linked-list/
Difficulty: Easy
Description: Given the head of a singly linked list, return true if it is a palindrome.
Follow up: Could you do it in O(n) time and O(1) space?"""

from typing import Optional
from package.data_structures import ListNode


class Solution:
    @staticmethod
    def isPalindrome(head: Optional[ListNode]) -> bool:
        """Optimal Solution: Reverse the second half of the linked list and compare
           the first half and the second half. Time Complexity: O(n), Space Complexity: O(1)"""
        # Base case: if head is None or head.next is None, return True
        if not head or not head.next:
            return True

        def reverse_linked_list(node: ListNode) -> ListNode:
            """Helper function to reverse a linked list: same as 0206-Reverse-Linked-List.py"""
            prev = None
            while node:
                next_node = node.next  # Save the next node for the next iteration
                node.next = prev  # Break the current's next node and point to the previous node
                prev, node = node, next_node  # Move to the next node by updating two pointers
            return prev

        # Find the middle of the linked list using pointers: similar to 0141-Linked-List-Cycle.py
        slow = fast = head
        while fast and fast.next:  # E.g. [1, 2, 3, 2, 1]
            slow, fast = slow.next, fast.next.next  # slow stops at 3, fast stops at 1

        # Reverse the second half of the linked list
        second_half = reverse_linked_list(slow)  # E.g. [3, 2, 1] -> [1, 2, 3]

        # Compare the first half and the second half of the linked list
        first_half = head  # E.g. [1, 2, 3, 2, 1]
        while second_half:  # Compare [1, 2, 3, 2, 1] and [1, 2, 3]
            if first_half.val != second_half.val:
                return False
            first_half, second_half = first_half.next, second_half.next
        return True


# Unit Test: Input: head = [1, 2, 2, 1]
head_test = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
assert Solution.isPalindrome(head_test) is True

# Unit Test: Input: head = [1, 2]
head_test = ListNode(1, ListNode(2))
assert Solution.isPalindrome(head_test) is False

# Unit Test: Input: head = [1, 2, 3, 2, 1]
head_test = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
assert Solution.isPalindrome(head_test) is True

print("All unit tests are passed")
